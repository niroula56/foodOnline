from django.urls import path
from . import views
from accounts import views as AccountView

urlpatterns = [
    path("", AccountView.vendorDashboard, name="vendor"),
    path("profile/", views.v_profile, name="v_profile"),
]