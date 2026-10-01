from django.urls import path
from . import views

urlpatterns=[
    path("index/",views.index),
    path("",views.index),
    path("about/",views.about),
    path("enquiry/",views.contact),
    path("gallery/",views.gallery),
    path("faculty/",views.team),
    path("branch/",views.branch),
    path("placements/",views.placements),
    path("facilities/",views.facilities),
    path("developer/",views.developer),
    path("contact/",views.contact),

]