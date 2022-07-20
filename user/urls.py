from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.main,name='main'),
    path('about/', views.about,name='about'),
    path('aboutus/', views.aboutus,name='aboutus'),
    path('registeruser/',views.registeruser,name='registeruser'),
    path('loginuser/',views.loginuser,name='loginuser'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    path('index/',views.index,name='index'),
    path('courses/',views.courses,name='courses'),
    path('coursesus/',views.coursesus,name='coursesus'),
    path('contact/', views.contact, name='contact'),
    path('contactus/', views.contactus, name='contactus'),
    path('logininst',views.logininst,name='logininst'),
    path('logoutinst/',views.logoutinst,name='logoutinst'),
    path('maininst/', views.maininst, name='maininst'),
    path('result/',views.result,name= 'result'),
    path('uploadtutorial/',views.uploadtutorial,name='uploadtutorial'),
    path('addquiz/',views.addquiz,name='addquiz'),
    path('coursesus/<str:slug>',views.tutorial,name='tutorial'),
    path('courses/<str:slug>',views.tutorial,name='tutorial'),
    path('quizes/',views.quizes,name='quizes'),
    path('quizes/<str:slug>',views.quiz,name='quiz'),
    path('search/', views.search, name='search'),
    path('search/<str:slug>',views.tutorial,name='tutorial'),
    path("reset_password",auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
    name="reset_password"),
    path("reset_password_sent",auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
    name="password_reset_done"),
    path("reset/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
    name="password_reset_confirm"),
    path("reset_password_complete",auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
    name="password_reset_complete"),

]