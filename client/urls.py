# from django.conf.urls import url
from django.urls import path, include
from .views import (
    OtpListApiView,
    VerifyOtpView,
    ImageView
)

urlpatterns = [
    path('api', OtpListApiView.as_view()),
    path('verify', VerifyOtpView.as_view()),
    path('images', ImageView.as_view()),
]