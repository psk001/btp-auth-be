# from django.conf.urls import url
from django.urls import path, include
from .views import (
    OtpListApiView,
    VerifyOtpView,
    ImageView,
    ElectionListView,
    ElectionCandidateListView
)

urlpatterns = [
    path('api', OtpListApiView.as_view()),
    path('verify', VerifyOtpView.as_view()),
    path('election', ElectionListView.as_view()),
    path('candidate', ElectionCandidateListView.as_view()),
    path('images', ImageView.as_view()),
]