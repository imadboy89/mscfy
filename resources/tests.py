from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Songs
from .serializers import SongsSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(title="", link=""):
        if title != "" and link != "":
            Songs.objects.create(title=title, link=link)

    def setUp(self):
        # add test data
        self.create_song(title="like glue", link="sean paul")
        self.create_song(title="simple song", link="konshens")
        self.create_song(title="love is wicked", link="brick and lace")
        self.create_song(title="jam rock", link="damien marley")


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("songs-all")
        )
        # fetch the data from db
        expected = Songs.objects.all()
        serialized = SongsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Create your tests here.
