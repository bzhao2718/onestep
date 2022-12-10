from .views import form_example01, form_example02, form_example03
from django.urls import path 

urlpatterns = [
    path("form-example01/", form_example01, name="form-example01"),
    path("form-example02/", form_example02, name="form-example02"),
    path("form-example03/", form_example03, name="form-example03"),
]
