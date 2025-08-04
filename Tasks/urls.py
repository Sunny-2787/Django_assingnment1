from django.urls import path
from Tasks.views import event ,Manager,form,update_form,delete_form
urlpatterns = [
    path('Event/',event),
    path('Boss/',Manager,name="Boss"),
    path('FROM/',form,name="form"),
    path('Update/<int:id>/',update_form,name="UPDATE"),
    path('delete/<int:id>/',delete_form,name="DELETE"),




]
