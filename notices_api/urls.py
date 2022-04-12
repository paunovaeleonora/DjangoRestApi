from django.urls import path

from notices_api import views

urlpatterns = (
    path('list/', views.ListNoticesView.as_view()),
    path('searchByDate/', views.SearchByDate.as_view()),
    path('searchByNoticeId/', views.SearchByNoticeId.as_view()),

)
