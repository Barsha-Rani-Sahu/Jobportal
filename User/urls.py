from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path('',views.home),
#----------------------------Recruiter---------------------------
    path('recruiter_home',views.Recruiter_home),
    path('recruiter_register',views.Recruiter_register),
    path('recruiter_login',views.Recruiter_login),
    path('post_job',views.Post_job),
    path('posted_jobs',views.Posted_jobs),
    path('logout',views.Logout),
    path('view_details/<job_id>',views.View_Details),
    path('applicant_details',views.Applicant),
    path('applicant_list/<job_id>',views.applicant_list),
#----------------------------Seeker---------------------------
    path('seeker_register',views.Seeker_register),
    path('seeker_login',views.Seeker_login),
    path('apply/<job_id>',views.Apply_job),
    path('view_job_details/<job_id>',views.View_job_Details),
    path('user_logout',views.user_logout),
    path('job_filter/<cat_name>/',views.job_filter),
    path('application_status/<name>',views.Application_status),
    path('fresher_jobs',views.Fresher_jobs),
    # path('latest_jobs',views.Latest_jobs),
    path('user_details',views.User_profile),
    path('my_profile',views.My_Profile),
    path('saved_jobs/<jobid>',views.Savedjob ,name='saved_jobs'),
    path('bookmark',views.Bookmark),
    # path('profile_edit/<user_id>',views.Profile_edit),
    path('applied_job',views.Applied_job),
]

