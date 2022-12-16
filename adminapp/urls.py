from django.urls import path
from adminapp import views 

urlpatterns = [
    path('admin-login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('new-staff/', views.add_newstaff, name='new-staff'),
    path('manage-staff/', views.manage_staff, name='manage-staff'),
    path('edit-staff/<int:id>/',views.edit_staff, name='edit-staff'),
    path('delete/<int:id>/', views.delete_staff, name='delete_staff'),
    path('published/',views.publishedcontent, name='published'),
    path('accept/<int:id>/', views.accept, name='accept'),
    path('reject/<int:id>/', views.reject, name='reject'),
    path('allcontent/',views.allcontent, name='allcontent'),
    path('delete_content/<int:id>/', views.delete_content, name='delete_content'),
    path('logout/',views.logout, name='admin_logout'),
]
