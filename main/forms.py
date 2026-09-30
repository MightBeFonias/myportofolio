from django.forms import DateTimeInput, ModelForm, TextInput, Textarea, URLInput, DateInput
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError
from main.models import Experience, Award


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description", 
            "category",
            "started_at",
            "ended_at"
            ]
        
        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Jenis Pengalaman",
            "started_at": "Waktu Mulainya Pengalaman",
            "ended_at": "Waktu Berakhirnya Pengalaman",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Pengalaman Kamu",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Masukkan Deskripsi Pengalaman Kamu",
                    "rows": 3,
                }
            ),
            "started_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama experience tidak boleh hanya berisi tag HTML.")
        return title

    def clean_category(self):
        return strip_tags(self.cleaned_data["category"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()
    
    def clean_started_at(self):
        return strip_tags(self.cleaned_data["started_at"]).strip()
    
    def clean_ended_at(self):
        return strip_tags(self.cleaned_data["ended_at"]).strip()

class AwardForm(ModelForm):
    class Meta:
        model = Award
        fields = [
            "title",
            "recognition",
            "description",
            "image",
            "awarded_at",
        ]

        labels = {
            "title" : "Judul Award",
            "recognition" : "Award yang Didapatkan",
            "description" : "Deskripsi Award",
            "image" : "Link GDrive Award",
            "awarded_at" : "Kapan Award Didapatkan",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Award Kamu",
                    "maxlength": 255,
                }
            ),
            "recognition": TextInput(
                attrs={
                    "placeholder": "Award yang Kamu Dapatkan",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Masukkan Deskripsi Pengalaman Kamu",
                    "rows": 3,
                }
            ),
            "image": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/...",
                }
            ),
            "awarded_at": DateInput(
                attrs={
                    "type": "date",
                }
            )
        }
    
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama award tidak boleh hanya berisi tag HTML.")
        return title

    def clean_recognition(self):
        return strip_tags(self.cleaned_data["recognition"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()
    
    def clean_image(self):
        return strip_tags(self.cleaned_data["image"]).strip()
    
    def clean_awarded_at(self):
        return strip_tags(self.cleaned_data["awarded_at"]).strip()
