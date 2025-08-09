from django.urls import path
from . import views

urlpatterns = [
    path('', views.loan_form_view, name='loan_form'),
]