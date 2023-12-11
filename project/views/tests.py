from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import Subject, Course, Subscription
from users.models import User


class SubjectTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='admin@admin.pro'
        )
        self.user.set_password('qwerty')
        self.user.save()

        get_token = reverse('user:token_obtain_pair')
        token_response = self.client.post(path=get_token, data={'email': 'admin@admin.pro', 'password': 'qwerty'})
        token = token_response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}

        self.course = Course.objects.create(
            name='test_Course',
            description='test'

        )

        self.subject = Subject.objects.create(
            name='test_Subject',
            course=self.course
        )

    def test_get_subject_list(self):
        """Тест получения спика предметов"""

        response = self.client.get(
            reverse('project:subject-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.subject.id,
                        "course": 2
                        ,
                        "name": self.subject.name,
                        "description": self.subject.description,
                        "preview": None,
                        "video": None,
                        "owner": self.subject.owner_id
                    }
                ]
            }

        )

    def test_subject_create(self):
        """"Тест создание урока"""

        data = {
            "name": "test2",
            "video": "https://www.youtube.com/",
        }

        response = self.client.post(reverse("project:subject-create"), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Subject.objects.all().count(), 2)

    def test_subject_create_validation_error(self):
        """"Тест валидации ссылок урока"""

        data = {
            "name": "test",
            "description": "https://stackoverflow.com/questions",
            "video": "https://stackoverflow.com/questions"
        }

        response = self.client.post(reverse('project:subject-create'), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.json(),
                         {'non_field_errors': ['Используются недопустимая ссылка']}
                         )

    def test_retrieve_subject(self):
        """"Тест просмотра детальной информации урока"""

        retrieve_url = reverse('project:subject-get', args=[self.subject.id])
        response = self.client.get(retrieve_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subject_update(self):
        """"Тест обновления информации урока"""

        data = {
            "name": "test_4",
            "video": "https://www.youtube.com/",
        }

        url = reverse("project:subject-update", args=[self.subject.pk])
        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson(self):
        """"Тест удаления урока"""

        delete_url = reverse('project:subject-delete', args=[self.subject.id])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Subject.objects.filter(id=self.subject.id).exists())


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='admin@admin.pro',
        )
        self.user.set_password('qwerty')
        self.user.save()

        get_token = reverse('user:token_obtain_pair')
        token_response = self.client.post(path=get_token, data={'email': 'admin@admin.pro', 'password': 'qwerty'})
        token = token_response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}

        self.course = Course.objects.create(
            name='test_course',
            description='test_course',
            owner=self.user
        )

    def test_create_subscription(self):
        """Тестирование создания подписки"""

        data = {
            "user": self.user.pk,
            "course": self.course.pk,
            "is_active": True
        }

        response = self.client.post(
            reverse('project:subscribe-create', kwargs={'pk': self.course.pk}),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_subscription(self):
        """Тестирование удаления подписки"""

        data = Subscription.objects.create(
            user=self.user,
            course=self.course
        )

        response = self.client.delete(
            reverse('project:subscribe-delete', kwargs={'pk': data.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
