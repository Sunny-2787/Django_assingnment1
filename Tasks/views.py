from django.shortcuts import render,redirect
from django.http import HttpResponse
from Tasks.models import Event, Participant
from datetime import date
from Tasks.forms import CatagoryForm,EventForm,ParticipantForm


def event_list(request):
    events = Event.objects.all()
    return render(request, "Event_man/event_list.html", {"events": events})


def event_detail(request, id):
    event = Event.objects.get(id=id)
    return render(request, "Event_man/event_detail.html", {"event":event})

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
    total_participants = Participant.objects.count()
    todays_events = Event.objects.filter(date=date.today())

    context={
        "total_events": total_events,
        "upcoming_events": upcoming_events,
        "past_events": past_events,
        "total_participants": total_participants,
        "todays_events": todays_events,
        "Total":Total

    }
    return render(request, "Event_man/dashboard.html", context)



def create_catagory(request):
    form = CatagoryForm()
    if request.method == "POST":
        form = CatagoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        
    return render(request,"Event_man/form.html",{"form" :form})

def create_participate(request):
    form = ParticipantForm()
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        
    return render(request,"Event_man/Participantform.html",{"form" :form})

def create_Event(request):
    form = EventForm
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        
    return render(request,"Event_man/Eventform.html",{"form" :form})


def Update_Event(request,id):
    event = Event.objects.get(id=id)
    form = EventForm(instance=event)
    if request.method == "POST":
        form = EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
            
    return render(request,"Event_man/Eventform.html",{"form" :form})

def DELETE_Event(request,id):


    if request.method == "POST":
        event = Event.objects.get(id=id)
        event.delete()

        return redirect("dashboard")
    else:
        return redirect("dashboard")
