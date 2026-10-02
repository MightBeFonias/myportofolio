from django.shortcuts import render, get_object_or_404, redirect, render
from main.models import Award, Experience
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from main.forms import ExperienceForm, AwardForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
import datetime
from django.views.decorators.http import require_POST

# Create your views here.
def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name" : "Fatih Naufal Habibillah",
        "npm" : "2506586394",
        "study_program" : "S1 Ilmu Komputer",
        "bio" : "CS student at Universitas Indonesia, now having a great emotional connection with Hermes, Codex, Opus, etc.",
        "last_login" : last_login
    }
    return render(request, "index.html", context)

def show_experience(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name" : "Fatih Naufal Habibillah",
        "title_query" : title_query,
        "form" : ExperienceForm(),
    }

    return render(request, 'experience.html', context)


def show_awards(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Fatih Naufal Habibillah",
        "title_query" : title_query,
        "form" : AwardForm(),
    }
    
    return render(request, "awards.html", context)

@login_required(login_url='/login/')
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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

@login_required(login_url='/login/')
def update_experience(request, experience_id):
    if not request.user.is_superuser and not request.user.groups.filter(name='Editor').exists():
        raise PermissionDenied

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

    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ', '.join([u.username for u in starred_users])

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category" : experience.category,
                "status" : experience.is_ongoing,
                "star_count" : starred_users.count(),
                "is_starred" : is_starred,
                "starred_by_names" : starred_by_names,
                "category_display": experience.get_category_display(),
                "star_count": starred_users.count(),
                "started_at": experience.started_at,
                "ended_at": experience.ended_at,
                "is_ongoing": experience.is_ongoing,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url = '/login/')
def create_award(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url='/login/')
def update_award(request, award_id):
    if not request.user.is_superuser and not request.user.groups.filter(name='Editor').exists():
        raise PermissionDenied
    
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

    data = []
    for award in awards:
        starred_users = award.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ', '.join([u.username for u in starred_users])

        data.append({
            "pk" : str(award.id),
            "fields" : {
                "title": award.title,
                "recognition": award.recognition,
                "description": award.description,
                "image": award.image,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
                "awarded_at" : award.awarded_at,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url='/login/')
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == 'POST':
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")
    
    return redirect("main:show_experience")

@login_required(login_url='/login/')
def delete_award(request, award_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    award = get_object_or_404(Award, pk=award_id)

    if request.method == "POST":
        award.delete()
        messages.success(request, "Award berhasil dihapus!")
        return redirect("main:show_awards")
    
    return redirect("main:show_awards")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silahkan login.")
        return redirect("main:login_user")
    
    context = {
        "name" : "Fatih Naufal Habibillah",
        "form" : form
    }

    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, form.get_user())
        response = redirect('main:show_main')
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H: %M: %S'))
        return response
    
    context = {
        "name" : "Fatih Naufal Habibillah",
        "form" : form,
    }

    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect('main:show_main')
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_star_award(request, award_id):
    award = get_object_or_404(Award, pk = award_id)

    if request.method == "POST":
        if request.user in award.starred_by.all():
            award.starred_by.remove(request.user)
        else:
            award.starred_by.add(request.user)

    return redirect("main:show_awards")

@require_POST
def create_award_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan award."},
            status=403,
        )

    form = AwardForm(request.POST)
    if form.is_valid():
        award = form.save()
        return JsonResponse(
            {"message": "Award berhasil ditambahkan.", "pk": str(award.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)