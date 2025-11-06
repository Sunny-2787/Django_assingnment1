from django.urls import path
from Tasks.views import event_list,dashboard,create_catagory,create_Event,event_detail,Update_Event,DELETE_Event,participant_list,RSVP_SYSTEM,user_dashboard,user_event_list, All_dashboard
urlpatterns = [
    path("events/", event_list, name="event_list"),
    path("participant_list/", participant_list, name="participant_list"),
    path("eventsDetail/<int:id> /", event_detail, name="event_Details"),
    
    path("dashboard/", dashboard, name="dashboard"),
    path("Add_catagory/", create_catagory, name="create_catagory_form"),
    # path("Add_participant/",create_participate , name="create_paricipant_form"),
    path("Add_Event/",create_Event , name="create_event_form"),
    path("Update_Event/<int:id>",Update_Event, name="Update_Event"),
    path("DELETE_Event/<int:id>",DELETE_Event, name="DELETE_Event"),
    path("RSVP/Event/<int:id>",RSVP_SYSTEM,name="RSVP_SYSTEM"),
    path("participant/Dashboard",user_dashboard,name="My list"),
    path("participant/Dashboard/viewAllevent",user_event_list,name="user_event_list"),
    path("Dashboard", All_dashboard,name="All_dashboard"),

]
