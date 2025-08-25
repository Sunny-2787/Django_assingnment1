from django.urls import path
from Tasks.views import event_list,dashboard,create_catagory,create_participate,create_Event,event_detail,Update_Event,DELETE_Event
urlpatterns = [
    path("events/", event_list, name="event_list"),
    path("eventsDetail/<int:id> /", event_detail, name="event_Details"),
    
    path("dashboard/", dashboard, name="dashboard"),
    path("Add_catagory/", create_catagory, name="create_catagory_form"),
    path("Add_participant/",create_participate , name="create_paricipant_form"),
    path("Add_Event/",create_Event , name="create_event_form"),
    path("Update_Event/<int:id>",Update_Event, name="Update_Event"),
    path("DELETE_Event/<int:id>",DELETE_Event, name="DELETE_Event"),




]
