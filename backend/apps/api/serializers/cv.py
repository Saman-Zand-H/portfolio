from rest_framework import serializers

from cv.models import CV, Project


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = ["about", "image", "location"]


class ProjectSerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Project
        exclude = ["id", "timestamp"]
        
    def get_technologies(self, obj):
        return [
            {"name": i.name, "icon": i.icon}
            for i in obj.technologies.all()
        ]
        
    def get_images(self, obj):
        return [
            {
                "image": i.image, 
                "alt": i.alt
            }
            for i in obj.images.all()
        ]
