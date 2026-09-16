from django.urls import path

from main.views import show_awards, show_main, show_experience, create_experience, create_award, get_experiences_json, get_awards_json, delete_experience, delete_award

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("awards/", show_awards, name="show_awards"),
    path("experience/add/", create_experience, name="create_experience"),
    path("api/experiences/", get_experiences_json, name="get_experiences_json"),
    path("awards/add/", create_award, name="create_award"),
    path("api/awards/", get_awards_json, name="get_awards_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("awards/<uuid:award_id>/delete/", delete_award, name="delete_award")
]