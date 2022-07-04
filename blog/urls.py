from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts),
    path('<str:name_post>', views.get_post_info),
    path('<int:number_post>', views.get_post_info_by_number),

]