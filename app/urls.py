"""
URL configuration for OnlineCourses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views 
from .views import BooksDetailView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('', views.index, name='index'),
     path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
     path('Manage_Courses', views.Manage_Courses, name='Manage_Courses'),
     path('Manage_Feedback', views.Manage_Feedback, name='Manage_Feedback'),
     path('Manage_Enquiry_details', views.Manage_Enquiry_details, name='Manage_Enquiry_details'),
     path('enquiry', views.enquiry, name='enquiry'),
     path('feedback', views.feedback, name='feedback'),
     path('Add_courses', views.Add_courses, name='Add_courses'),
     path('addCourse', views.addCourse, name='addCourse'),
     path('Register_page', views.Register_page, name='Register_page'),
     path('detail/<int:pk>/', views.detail, name='detail'),
     path('<int:pk>/', BooksDetailView.as_view(), name = 'detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)