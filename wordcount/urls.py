"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin   # for now we don't need this admin stuff
from django.urls import path
from . import views

# every time someone visits the site (connected to this django project),
# it's gonna come to this file and this list of urlpatterns decides where
# the user's request should go next and what html to send back to user
# in other words it's a starting point of our django website
# when in brouser user changes url from default localhost:8000 to localhost:8000/whatever,
# then it comes here and checks where is such a url in this list
urlpatterns = [
    # path('admin/', admin.site.urls), # localhost:8000/admin takes user to admin page
    # path('eggs/', admin.site.urls),  # localhost:8000/eggs again takes user to admin page
    path('', views.homepage, name='home'), # if someone comes to homepage, that's '' stands for, so it comes after localhost:8000, then 2nd argument here is where we want to take our user
    # so we need to create views.py which will allow us to send back information (create it in same folder as this urls file)
    # also we need to import views.py to make it visible here. Then we need to create a method inside views.py to pass in.
    path('eggs/', views.eggs), # another page on site, which is processed by views.eggs function, /-slash is obligatory
    path('count/', views.count, name='count'), # 3rd parameter "name" is attr that we're tied to in home.html, we need it because if
                                              # we want to change "count/" address to other one, it will break the page
                                              # using name='count' we can rename page address 'count' to 'countthewords' or whatever
                                              # from here it goes to count.html using views.count function
    path('about/', views.about, name='about'),
]
