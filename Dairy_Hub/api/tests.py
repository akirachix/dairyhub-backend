
from django.test import TestCase

Create your tests here.

from rest_framework.test import APITestCase

from rest_framework import status

from django.urls import reverse

from Orders.models import Order


class OrderTests(APITestCase):
    def setUp(self):
        self.farmer = farmer.objects.create(full_name="Mwkali", email="mukali@gmail.com", phone="0724973222")
        self.Order_data = {
            "status": "Pending",
            "price": "1000.00",
            "order_date":"2025-06-11",
            "farmer_id": self.farmer.id,
        }

    def test_post_Order(self):
        url = reverse('Orders-list')
        response = self.client.post(url, self.Order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_Order(self):
        Order.objects.create(**self.Order_data)
        url = reverse('Orders-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_put_Order(self):
        Order.objects.create(**self.Order_data)
        order = Order.objects.first()
        url = reverse('Orders-detail', args=[order.id])
        response = self.client.put(url, self.Order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

     
    def test_delete_Order(self):
        Order.objects.create(**self.Order_data)
        order = Order.objects.first()
        url = reverse('Orders-detail', args=[order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    


    
    




