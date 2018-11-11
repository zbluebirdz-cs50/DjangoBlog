from django.urls import path
from . import views

urlpatterns = [
    # default page/view:
    path("", views.post_list, name="post_list"),
    path("post<int:pk>/", views.post_detail, name="post_detail"),
]