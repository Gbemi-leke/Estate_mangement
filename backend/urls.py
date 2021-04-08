from django.urls import path
from django.conf.urls import url 
from backend import views

app_name = 'backend'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('login-admin/', views.login2_view, name='login2_view'),
    path('logout_view-page/', views.logout_view, name='logout_view'),
    path('password_reset/', views.password_reset_request, name='password_reset_request'),
    path('dashboard-page/', views.dashboard, name='dashboard'),
    path('user_profile-page/', views.user_profile, name='user_profile'),
    path('edit_form-page/', views.edit_form, name='edit_form'),
    path('add_agent-page/', views.add_agent, name='add_agent'),
    path('agent-page/', views.agent, name='agent'),
    path('view_agent-page/<int:agent>', views.view_agent, name='view_agent'),
    path('delete_agent-page/<int:liste_id>', views.delete_agent, name='delete_agent'),
    path('edit_newform-page/', views.edit_newform, name='edit_newform'),
    path('pass_form-page/', views.pass_form, name='pass_form'),
    path('reset/', views.reset, name='reset'),
    path('success-message/', views.success_message, name='success_message'),
    path('register-page/', views.register_form, name='register_form'),
    path('logout/', views.logout_view, name='logout_view'),
    path('view-newlisting/<int:pk>', views.view_newlistingdetails, name='view_newlistingdetails'),
    path('delete-property/<int:listf_id>', views.delete_newproperty, name='delete_newproperty'),
    path('add-newlisting-page/', views.add_newlisting, name='add_newlisting'),
    path('listings-page/', views.new_listings, name='new_listings'),
    path('listings-page/<int:post_id>', views. edit_newlisting, name=' edit_newlisting'),
    path('list-users/', views.list_users, name='list_users'),
    path('list-all-post/', views.list_all_post, name='list_all_post'),
    path('delete_upload/<int:del_id>', views.delete_upload, name='delete_upload'),
    # path('reset-password/',auth_views.PasswordResetView.as_view(template_name='registration/reset-password.html', email_template_name='registration/password-reset-email.html', success_url = reverse_lazy('backend:password_reset_done'), form_class=PasswordReset), name='password_reset'),
    # path('password-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password-confirm-form.html',form_class=SetPassword, success_url = reverse_lazy('backend:password_reset_complete')), name='password_reset_confirm'),
   
]