from django.shortcuts import render
from main.models import Experience

# Create your views here.
def show_main(request):
    context = {
        "name" : "Fatih Naufal Habibillah",
        "npm" : "2506586394",
        "study_program" : "S1 Ilmu Komputer",
        "bio" : "CS student at Universitas Indonesia, now having a great emotional connection with Hermes, Codex, Opus, etc."
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name" : "Fatih Naufal Habibillah",
        "experience_list" : Experience.objects.all(),
    }
    return render(request, 'experience.html', context)