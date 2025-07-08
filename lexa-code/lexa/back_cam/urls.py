from django.urls import path
from . import views

urlpatterns = [
    path("",views.back_cam),
    path("nav",views.photo_stream,name="nav"),
    path("back_cam_stream",views.back_cam_stream, name="back_cam_stream"),
    path('serit_takip_stream/', views.serit_takip_stream, name='serit_takip_stream'),
    path("get_request",views.get_request,name="get_request"),
    path("post_request",views.post_request,name="post_request"),
    path("tr_stream",views.tr_stream,name="tr_stream")
]
