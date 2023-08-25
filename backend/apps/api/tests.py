from rest_framework import status
from django.urls import reverse_lazy
from django.test import override_settings
from rest_framework.test import APITestCase

from api.utils import random_str
from cv.models import CV, Project, Technology
from api.serializers.cv import CVSerializer, ProjectSerializer, TechnologySerializer


@override_settings(SECURE_SSL_REDIRECT=False)
class TestCV(APITestCase):
    fixtures = ["fixtures/cv.json"]

    def test_cv_is_singletone(self):
        self.assertEqual(CV.objects.count(), 1)

    def test_list_cv_success(self):
        url = reverse_lazy("api:cv-list")
        # in order to get the right path for media and staticfiles
        response = self.client.get(url)
        serialized_data = CVSerializer(CV.objects.all(), many=True)
        serialized_data.context["request"] = response.wsgi_request
        expected_data = serialized_data.data
        print(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_data, response.json())

    def test_retrieve_cv_success(self):
        cv_instance = CV.objects.first()
        url = reverse_lazy("api:cv-detail", args=[cv_instance.pk])
        # in order to get the right path for media and staticfiles
        response = self.client.get(url)
        seralized_data = CVSerializer(cv_instance)
        seralized_data.context["request"] = response.wsgi_request
        expected_data = seralized_data.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_data, response.json())

    def test_list_cv_read_only(self):
        url = reverse_lazy("api:cv-list")
        data = {i.name: random_str() for i in CV._meta.get_fields()}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_retrieve_cv_read_only(self):
        cv_instance = CV.objects.first()
        url = reverse_lazy("api:cv-detail", args=[cv_instance.pk])
        data = {i.name: random_str() for i in CV._meta.get_fields()}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


@override_settings(SECURE_SSL_REDIRECT=False)
class TestProject(APITestCase):
    fixtures = ["fixtures/cv.json"]

    def test_list_projects_success(self):
        url = reverse_lazy("api:project-list")
        # in order to get the right path for media and staticfiles
        response = self.client.get(url)
        serialized_data = ProjectSerializer(Project.objects.all(), many=True)
        serialized_data.context["request"] = response.wsgi_request
        expected_data = serialized_data.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_data, response.json())

    def test_retrieve_project_success(self):
        project_instance = Project.objects.first()
        url = reverse_lazy("api:project-detail", args=[project_instance.pk])
        # in order to get the right path for media and staticfiles
        response = self.client.get(url)
        seralized_data = ProjectSerializer(project_instance)
        seralized_data.context["request"] = response.wsgi_request
        expected_data = seralized_data.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_data, response.json())

    def test_list_projects_read_only(self):
        url = reverse_lazy("api:project-list")
        data = {i.name: random_str() for i in Project._meta.get_fields()}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_retrieve_project_read_only(self):
        project_instance = Project.objects.first()
        url = reverse_lazy("api:project-detail", args=[project_instance.pk])
        data = {i.name: random_str() for i in Project._meta.get_fields()}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


@override_settings(SECURE_SSL_REDIRECT=False)
class TestTechnology(APITestCase):
    fixtures = ["fixtures/cv.json"]

    def test_list_technologies_success(self):
        url = reverse_lazy("api:technology-list")
        # in order to get the right path for media and staticfiles
        response = self.client.get(url)
        serialized_data = TechnologySerializer(Technology.objects.all(), many=True)
        serialized_data.context["request"] = response.wsgi_request
        expected_data = serialized_data.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_data, response.json())

    def test_retrieve_technology_success(self):
        technology_instance = Technology.objects.first()
        url = reverse_lazy("api:technology-detail", args=[technology_instance.pk])
        # in order to get the right path for media and staticfiles
        response = self.client.get(url)
        seralized_data = TechnologySerializer(technology_instance)
        seralized_data.context["request"] = response.wsgi_request
        expected_data = seralized_data.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_data, response.json())

    def test_list_technologies_read_only(self):
        url = reverse_lazy("api:technology-list")
        data = {i.name: random_str() for i in Technology._meta.get_fields()}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_retrieve_technology_read_only(self):
        technology_instance = Technology.objects.first()
        url = reverse_lazy("api:technology-detail", args=[technology_instance.pk])
        data = {i.name: random_str() for i in Technology._meta.get_fields()}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
