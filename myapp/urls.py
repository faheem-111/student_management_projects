from django.contrib import admin
from django.urls import path,include

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'),
    path('login_page/',views.login_page,name='login_page'),
    path('dashboard_page/',views.dashboard_page,name='dashboard_page'),
    path('HODdashboard_page/',views.HODdashboard_page,name='HODdashboard_page'),
    path('staffboard_page/',views.staffboard_page,name='staffboard_page'),
    path('profile_page/',views.profile_page,name='profile_page'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('addstaff_page/',views.addstaff_page,name='addstaff_page'),
    path('viewstaff_page/',views.viewstaff_page,name='viewstaff_page'),
    path('addcourse_page/',views.addcourse_page,name='addcourse_page'),
    path('viewcourse_page/',views.viewcourse_page,name='viewcourse_page'),
    path('addsubject_page/',views.addsubject_page,name='addsubject_page'),
    path('viewsubject_page/',views.viewsubject_page,name='viewsubject_page'),
    path('editstaff_page/<str:id>',views.editstaff_page,name='editstaff_page'),
    path('updatestaff_page/',views.updatestaff_page, name='updatestaff_page'),
    path('deletestaff_page/<int:admin>/', views.deletestaff_page, name='deletestaff_page'),
    path('editcourse_page/<str:id>', views.editcourse_page, name='editcourse_page'),
    path('updatecourse_page/', views.updatecourse_page, name='updatecourse_page'),
    path('deletecourse_page/<int:id>/', views.deletecourse_page, name='deletecourse_page'),
    path('editsubject_page/<str:id>', views.editsubject_page, name='editsubject_page'),
    path('updatesubject_page/',views.updatesubject_page, name='updatesubject_page'),
    path('deletesubject_page/<int:id>',views.deletesubject_page, name='deletesubject_page'),
    path('addsession_page/',views.addsession_page, name='addsession_page'),
    path('viewsession_page/',views.viewsession_page, name='viewsession_page'),
    path('editsession_page/<str:id>',views.editsession_page, name='editsession_page'),
    path('updatesession_page/',views.updatesession_page, name='updatesession_page'),
    path('deletesession_page/<str:id>', views.deletesession_page, name='deletesession_page'),
    path('sendstaffnotification_page/', views.sendstaffnotification_page, name='sendstaffnotification_page'),
    path('savestaffnotifications_page',views.savestaffnotifications_page, name='savestaffnotifications_page'),
    path('viewnotification_page',views.viewnotification_page, name='viewnotification_page'),
    path('feedback_page',views.feedback_page, name='feedback_page'),
    path('savefeedback_page', views.savefeedback_page, name='savefeedback_page'),
    path('feedbackview_page', views.feedbackview_page, name='feedbackview_page'),
    path('feedbacksave_page', views.feedbacksave_page, name='feedbacksave_page'),
    path('dologout/', views.dologout, name='dologout'),




]