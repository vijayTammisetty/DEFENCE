from django.urls import path
from . import views
urlpatterns = [
    path('user-login/', views.user_login, name='user-login'),
    # path('registration/', views.user_registration, name='registration'),
    path('dashbord', views.user_dashbord, name='dashbord'),
    path('profile/',views.profile, name='profile'),
    path('conf-data/', views.confidencial_data, name='conf-data'),
    path('record/',views.request_record, name='record'),
    path('send_request/<int:id>/', views.send_request, name='send_request'),
    path('approved-record/', views.approved_record, name='approved-record'),
    path('view-record/<int:id>/', views.view_record, name='view_record'),
    path('received_files/',views.received_records, name='received_files'),
    path('searched_received_files/', views.search_file, name='search'),
    path('delete_file/<int:id>/',views.delete_file, name='delete_file'),
    path('logout/', views.user_logout, name='logout'),
]


