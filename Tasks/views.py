from django.shortcuts import render,redirect
from django.http import HttpResponse
from Tasks.models import Event,RSVP
from datetime import date
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.models import User
from Tasks.forms import CatagoryForm,EventForm,RSVPForm
from django.contrib.auth.decorators import user_passes_test,login_required,permission_required
from users.views import is_admin

def is_organiger(user):
    return  user.groups.filter(name="Organizer").exists()


def is_participant(user):
    return user.groups.filter(name="participant").exists()

# def is_admin(user):
#     return user.groups.filter(name="admin").exists()


@login_required

def event_list(request):
    events = Event.objects.all()
    return render(request, "Event_man/event_list.html", {"events": events})

@user_passes_test(is_participant)
def user_event_list(request):
    event= Event.objects.all()
    return render(request, "Event_man/user_event_view.html", {"events": event})


def participant_list(request):
    participants = RSVP.objects.all().prefetch_related('user','event')
    return render(request, "Event_man/participantlist.html", {"rsvps": participants})

@login_required
@user_passes_test(is_organiger or is_admin)
def event_detail(request, id):
    event = Event.objects.get(id=id)
    return render(request, "Event_man/event_detail.html", {"event":event})

@login_required
@user_passes_test(is_organiger,login_url="no-permission")
def dashboard(request):
    
    type = request.GET.get("type",'all')
    if type == "upcoming":
        Total = Event.objects.filter(date__gt=date.today())
    elif type == "past":
        Total = Event.objects.filter(date__lt=date.today())
    else:
        Total = Event.objects.prefetch_related("participants").all()

    

    total_events  = Event.objects.count()
    upcoming_events = Event.objects.filter(date__gte=date.today()).count()
    past_events = Event.objects.filter(date__lt=date.today()).count()
    total_participants =RSVP.objects.values('user').distinct().count()
    todays_events =Event.objects.filter(date=date.today()).annotate(participant_count=Count('event_rsvps'))

    context={
        "total_events": total_events,
        "upcoming_events": upcoming_events,
        "past_events": past_events,
        "total_participants": total_participants,
        "todays_events": todays_events,
        "Total":Total

    }
    return render(request, "Event_man/dashboard.html", context)


@login_required
@permission_required("Tasks.add_catagory")
def create_catagory(request):
    form = CatagoryForm()
    if request.method == "POST":
        form = CatagoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("event_list")
        
    return render(request,"Event_man/form.html",{"form" :form})

# def create_participate(request):
#     form = ParticipantForm()
#     if request.method == "POST":
#         form = ParticipantForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("dashboard")
        
#     return render(request,"Event_man/Participantform.html",{"form" :form})
@login_required
@permission_required("Tasks.add_event")
def create_Event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("event_list")
        
    return render(request,"Event_man/Eventform.html",{"form" :form})

@login_required
@permission_required("Tasks.change_event")
def Update_Event(request,id):
    event = Event.objects.get(id=id)
    form = EventForm(instance=event)
    if request.method == "POST":
        form = EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect("event_list")
            
    return render(request,"Event_man/Eventform.html",{"form" :form})


@login_required
@permission_required("Tasks.delete_event")
def DELETE_Event(request,id):


    if request.method == "POST":
        event = Event.objects.get(id=id)
        event.delete()

        return redirect("event_list")
    else:
        return redirect("event_list")

@login_required
@user_passes_test(is_participant)
def RSVP_SYSTEM(request,id):
    event=Event.objects.get(id=id)
    if request.method=="POST":
        
        if not request.user.is_authenticated:
            messages.success(request, "You must be logged in to RSVP.")
            return redirect('event_list')
    
        already_rsvped = RSVP.objects.filter(user=request.user, event=event).exists()
        if already_rsvped:
            messages.warning(request, "You have already RSVP'd for this event.")
        else:
            status = request.POST.get('status', 'interested')
        
            RSVP.objects.create(user=request.user, event=event, status=status)
            messages.success(request, f"You RSVP'd as '{status}' successfully!")

            return redirect('user_event_list')  

    return redirect('user_event_list')

@login_required
@user_passes_test(is_participant)
def user_dashboard(request):
    rsvps = RSVP.objects.filter(user=request.user).select_related('event')
    return render(request,"Event_man/user_dashboard.html",{'rsvps':rsvps})


@login_required
def All_dashboard(request):
    if is_organiger(request.user):
        return redirect('dashboard')
    elif  is_admin(request.user):
        return redirect('admin')
    elif is_participant:
        return redirect('My list')
    else:
        return redirect("no-permission")
        