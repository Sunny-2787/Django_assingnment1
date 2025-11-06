from django.urls import path
from users.views import sing_up,login_in,out,activate_user,admin_dashboard,assign_role,create_group,group_list,delet_group,delet_user

urlpatterns =[
    path("sing-up/",sing_up,name= 'sing-up'),
    path("log-in/",login_in,name= 'login'),
    path("log-out/",out,name= 'out'),
    path("activate/<int:user_id>/<str:token>/",activate_user),
    path("Admin_Dashboard",admin_dashboard,name="admin"),
    path("NewRole/<int:user_id>/",assign_role,name="role"),
    path("Create_New_Group/",create_group,name="create_group"),
    path("group_list/Check/",group_list,name="group_list"),
    path("group_Delete/<int:id>/",delet_group,name="group_delet"),
    path("User_Delete/<int:id>/",delet_user,name="delet_user"),
    
    
]