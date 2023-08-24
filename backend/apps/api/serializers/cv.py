from rest_framework import serializers

from cv.models import CV, Project, Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["name", "icon", "url"]


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
        request = self.context.get("request")
        return [
            {
                "name": i.name,
                "icon": request.build_absolute_uri(i.icon.url),
                "url": i.url,
            }
            for i in obj.technologies.all()
        ]

    def get_images(self, obj):
        request = self.context.get("request")
        return [
            {"image": request.build_absolute_uri(i.image.url), "alt": i.alt}
            for i in obj.images.all()
        ]
