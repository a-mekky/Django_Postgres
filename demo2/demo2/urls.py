"""demo2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from affairs.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('contact_us/', contactus, name='contact_us'),
    path('about_us/', aboutUS, name='about_us'),
    path('', login, name=''),
    path('register/', addUser, name='register'),
    path('addStudent/', addStudent, name='addStudent'),
    path('viewStudent/', viewStudent, name='viewStudent'),
    path('deletestudent/<id>', deletestudent, name='deletestudent'),
    path('updatestudent/<id>',updatestudent,name='updatestudent'),
    path('logout/',user_logout,name='logout'),

    # New Day 3  ######## All Are Running At addStudentModel
    path('addStudentForm/',addStudentForm,name='addStudentForm'),
    path('addStudentModel/',addStudentModel,name='addStudentModel'),

    #Edit
    path('addintake/',addIntakeModel,name='addIntake'),
    path('addtrack/',addTrackModel,name='addtrack'),

    # New API
    path('myapi/',include('myapi.urls')),
]



