from django.utils.html import strip_tags
from rest_framework import serializers
from django.utils import timezone

from main.models import Experience, Award

class ExperienceSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    category_display = serializers.CharField(source="get_category_display", read_only=True)

    class Meta:
        model = Experience
        fields = [
            'id', 'title', 'description', 'category', 'category_display', 'started_at', 
            'ended_at', 'is_starred', 'star_count', 'starred_by_names',
        ]
        read_only_fields = ['id']
    
    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError('Title cannot be empty.')
        return value
    
    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError('Title cannot be empty.')
        return strip_tags(value)
    
    def validate_category(self, value):
        return strip_tags(value)
    
    def validate_started_at(self, value):
        if value > timezone.now():
            raise serializers.ValidationError('Start time cannot be in the future.')
        return value
    
    def get_star_count(self, obj):
        return obj.starred_by.count()
    
    def get_is_starred(self, obj):
        request = self.context.get('request')
        if request is None or not request.user.is_authenticated: 
            return False
        return request.user in obj.starred_by.all()
    
    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())
    
class AwardSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Award
        fields = [
            'id', 'title', 'recognition', 'description', 
            'image', 'awarded_at', 'starred_by_names', 'star_count',
            'is_starred',
        ]
        read_only_fields = ['id']
    
    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError('Title cannot be empty.')
        return value
    
    def validate_recognition(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError('Title cannot be empty.')
        return value
    
    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError('Title cannot be empty.')
        return value
    
    def validate_awarded_at(self, value):
        if value > timezone.localdate():
            raise serializers.ValidationError('Award cannot be given in the future.')
        return value
        
    def get_star_count(self, obj):
        return obj.starred_by.count()
    
    def get_is_starred(self, obj):
        request = self.context.get('request')
        if request is None or not request.user.is_authenticated: 
            return False
        return request.user in obj.starred_by.all()
    
    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())
    
