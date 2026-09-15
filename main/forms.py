from django.forms import DateTimeInput, ModelForm, TextInput, Textarea, URLInput, DateInput

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
            "award_image_url": URLInput(
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
