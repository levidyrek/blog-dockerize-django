from django.urls import path

from . import views

urlpatterns = [
    path('submit/', views.SubmitJobApplicationView.as_view(),
         name='Submit Job Application'),
    path('submit/success/', views.application_success,
         name='Job Application Submission Success')
]
