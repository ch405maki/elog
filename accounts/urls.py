from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('visitor', views.visitor, name='visitor.index'),
    path('submit-log/', views.save_visitor_log, name='submit_log'),

    path('visitors/pending/', views.pending_visitors, name='pending_visitors'),
    path('visitors/approved/', views.approved_visitors, name='approved_visitors'),
    path('visitor-out/', views.visitor_out_view, name='visitor_out'),
    path('visitor-out/<int:visitor_id>/', views.mark_visitor_out, name='visitor_out_action'),

    path('approve/<int:id>/', views.approve_visitor, name='approve_visitor'),
    path('decline/<int:id>/', views.decline_visitor, name='decline_visitor'),

    path('reports/', views.visitor_reports, name='visitor_reports'),

    path('accounts/', views.account_index, name='account_index'),
    path('accounts/manage', views.account_manage, name='account_manage'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('accounts/<int:user_id>/', views.user_detail, name='user_detail'),
    path('accounts/create/', views.create_user, name='create_user'),
    

]
