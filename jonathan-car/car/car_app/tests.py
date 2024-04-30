# tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Car

class CarTestCase(TestCase):
    def test_car_creation(self):
        car = Car.objects.create(name='Toyota', color='Red', position=1)
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'car_app/car_list.html')
        self.assertEqual(car.name, 'Toyota')
        self.assertContains(response, car.name)
    def test_show_car(self):
        car = Car.objects.create(name='Toyota', color='Red', position=1)
        response = self.client.get(reverse('show_car', kwargs={'color': car.color}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Toyota')

    def test_update_car(self):
        car = Car.objects.create(name='Toyota', color='Red', position=1)
        update_url = reverse('update_car', kwargs={'pk': car.pk})
        updated_color = 'Blue'
        response = self.client.post(update_url, {'name': updated_color, 'color': car.color, 'position': car.position})
        self.assertEqual(response.status_code, 302)
        car.refresh_from_db()
        self.assertEqual(car.name, updated_color)
    def test_car_deletion(self):
        car = Car.objects.create(name='Toyota', color='Red', position=1)
        delete_url = reverse('delete_car', kwargs={'pk': car.pk})
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        car_exists = Car.objects.filter(pk=car.pk).exists()
        self.assertFalse(car_exists)