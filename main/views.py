from django.shortcuts import render, get_object_or_404, redirect, render
from main.models import Award, Experience
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.forms import ExperienceForm, AwardForm

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
    json_response = get_experiences_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8")
    )

    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name" : "Fatih Naufal Habibillah",
        "experience_list" : experiences,
        "title_query" : title_query,
    }
    return render(request, 'experience.html', context)


def show_awards(request):
    json_response = get_awards_json(request)

    awards = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8")
    )

    awards = [award.object for award in awards]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Fatih Naufal Habibillah",
        "awards": awards,
        "title_query" : title_query,
    }
    return render(request, "awards.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Fatih",
        "form": form,
    }
    return render(request, "form_experience.html", context)

def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Fatih",
        "form": form,
        "experience": experience,
        "is_update": True,
    }
    return render(request, "form_experience.html", context)

def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def create_award(request):
    form = AwardForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Award baru berhasil ditambahkan!")
        return redirect("main:show_awards")

    context = {
        "name": "Fatih",
        "form": form,
    }
    return render(request, "form_award.html", context)

def update_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)
    form = AwardForm(request.POST or None, instance=award)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Award berhasil diperbarui!")
        return redirect("main:show_awards")

    context = {
        "name": "Fatih",
        "form": form,
        "award": award,
        "is_update": True,
    }
    return render(request, "form_award.html", context)

def get_awards_json(request):
    title_query = request.GET.get("title", "").strip()
    awards = Award.objects.all()

    if title_query:
        awards = awards.filter(title__icontains=title_query)

    awards_json = serializers.serialize("json", awards)
    return HttpResponse(awards_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == 'POST':
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")
    
    return redirect("main:show_experience")

def delete_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)

    if request.method == "POST":
        award.delete()
        messages.success(request, "Award berhasil dihapus!")
        return redirect("main:show_awards")
    
    return redirect("main:show_awards")