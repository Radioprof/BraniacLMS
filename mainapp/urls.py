from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig


app_mame = MainappConfig.name


urlpatterns = [
    path('contacts/', views.ContactsView.as_view()),
    path('courses/', views.CoursesView.as_view()),
    path('docsite/', views.DocSiteView.as_view()),
    path('', views.IndexView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('news/', views.NewsView.as_view()),

]
