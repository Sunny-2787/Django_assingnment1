from django.shortcuts import render,redirect
from django.http import HttpResponse
from Tasks.models import Event, Participant
from datetime import date
from Tasks.forms import Eventform,participanForm
# Create your views here.
# def h(request):
#     return HttpResponse("Fello")

def event(request):
    # type=request.GET.get("type","all")
    Total = Event.objects.all()
   
    participant_all=Participant.objects.count()
    context = {
        "Total": Total,

        
        "participant_all":participant_all,
    }
    

    return render (request,'Event_man/eventDa.html',context)



def Manager(request):
    type = request.GET.get("type",'all')
    if type == "UPe":
        Total = Event.objects.filter(date__gt=date.today())
    elif type == "PAe":
        Total = Event.objects.filter(date__lt=date.today())
    elif type == "TOe":
        Total = Event.objects.filter(date=date.today())
    else:
        Total = Event.objects.all()
    # print(type)
    # Total = Event.objects.all()
    event_all = Event.objects.count()
    participant_all=Participant.objects.count()

    upcoming_E= Event.objects.filter(date__gt=date.today()).count()
    Past_E = Event.objects.filter(date__lt=date.today()).count()
    # events_today = Event.objects.filter(date__date=date.today())


    context = {
        "Total": Total,

        "event_all":event_all,
        "participant_all":participant_all,
        "upcoming_E" : upcoming_E,
        "Past_E":Past_E,
        # "events_today":events_today 
    }



    return render (request,'Event_man/Manager-Dash.html',context)




def form(request):
    form = Eventform()
    p_form = participanForm()
   

    if request.method == "POST":
        form = Eventform(request.POST)
        p_form = participanForm(request.POST)
        
        if form.is_valid() and  p_form.is_valid():
            form.save()
            p_form.save()

        
    

    return render(request, 'Event_man/form.html', {
        "form": form,
        "p_form":p_form
        
    })

def update_form(request,id):
    Total = Event.objects.get(id=id)

    form = Eventform(instance=Total)
   
    p_form = participanForm()
   

    if request.method == "POST":
        form = Eventform(request.POST,instance=Total)
        p_form = participanForm(request.POST)
        
        if form.is_valid() and  p_form.is_valid():
            form.save()
            p_form.save()

        
    

    return render(request, 'Event_man/form.html', {
        "form": form,
        "p_form":p_form
        
    })

def delete_form(request,id):
    if request.method =="POST":
        Total = Event.objects.get(id=id)
        Total.delete()

    return redirect('Boss')

        

