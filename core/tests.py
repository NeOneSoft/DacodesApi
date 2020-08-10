# Django
from django.contrib.auth.models import User
from django.urls import path, include
# Djangorestframeworkç
from rest_framework.test import RequestsClient, APITestCase



# API token test
class TokenTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin', email='admin@gmail.com')

    def test_authenticate(self):
        result = self.client.post('/api/token/', {'username': 'admin', 'password': 'admin'})

        assert 'access' in result.data

    def test_valid_token(self):
        result = self.client.post('/api/token/', {'username': 'admin', 'password': 'admin'})
        token = result.data['access']

        courses_result = self.client.get('/api/v1/courses/', HTTP_AUTHORIZATION='Bearer {0}'.format(token))

        assert courses_result.status_code == 200


# API Urls test
class CourseApiTest(APITestCase):
    urlpatterns = [
        path('api/v1/', include('core.urls.v1')),
    ]

    def test_courses_url(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/v1/courses/')

        self.assertEqual(response.status_code, 403)

    def test_lessons_url(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/v1/lessons/')

        self.assertEqual(response.status_code, 403)

    def test_questions_url(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/v1/questions/')

        self.assertEqual(response.status_code, 403)
