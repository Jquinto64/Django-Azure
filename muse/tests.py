from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Section
from .serializers import SectionSerializer

# Create your tests here
class BaseViewTest(APITestCase):
    client = APIClient()
    
    @staticmethod
    def create_section(title="", description=""):
        if title != "" and description != "":
            Section.objects.create(title = title, description = title)
    def setUp(self):
        self.create_section("intro", "test intro")
        self.create_section("resuls", "test results")
        self.create_section("hello", "jonny")
        
class GetAllSectionsTest(BaseViewTest):
    def test_getAllSections(self):
        response = self.client.get(reverse("sections-all", kwargs={"version": "v1"}))
        
        expected = Section.objects.all()
        serialized = SectionSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)