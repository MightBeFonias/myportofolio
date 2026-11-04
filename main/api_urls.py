from django.urls import path
from main import api_views

app_name = 'api'
urlpatterns = [
    path('experience/', api_views.experience_list, name='experience-list'),
    path('awards/', api_views.award_list, name='award-list'),
    path("experience/<uuid:experience_id>/", api_views.experience_detail, name="experience-detail"),
    path("awards/<uuid:award_id>/", api_views.award_detail, name="award-detail"),
    path("experience/<uuid:experience_id>/star/", api_views.experience_star, name="experience-star"),
    path("awards/<uuid:award_id>/star/", api_views.award_star, name="award-star"),
]