import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='Full-Time')
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(blank=True, null=True)

    starred_by = models.ManyToManyField(
        User, related_name="starred_experiences", blank=True
    )

    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None


class Award(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    recognition = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(blank=True)
    awarded_at = models.DateField()

    starred_by = models.ManyToManyField(
        User, related_name="starred_awards", blank=True
    )

    class Meta:
        ordering = ["-awarded_at"]

    def __str__(self):
        return self.title
    
User = get_user_model()

def is_editor(self):
    return self.groups.filter(name='Editor').exists()

User.add_to_class('is_editor', is_editor)