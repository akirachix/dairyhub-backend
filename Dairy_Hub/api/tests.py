
from django.test import TestCase

Create your tests here.
from django.test import TestCase

# # Create your tests here.

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
    


    
    



from suppliers.models import Supplier

from products.models import Product

from orders.models import orders

from orderItems.models import OrderItem


class ProductTests(APITestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name="Mwkali", email="mukali@gmail.com", phone="0724973222")
        self.product_data = {
            "name": "Milking Cans",
            "category": "Dairy Equipments",
            "description": "Milking cans are commonly used on dairy farms and are essential for maintaining the freshness and hygiene of milk during its journey from the cow to processing or consumption. ",
            "price": "1000.00",
            "stock": 20,
            "supplierid": self.supplier.id,
            "product_image_url": "https://kenyaagri.com/wp-content/uploads/2024/09/Stainles-milk-cans.jpg"
        }

    def test_create_product(self):
        url = reverse('products-list')
        response = self.client.post(url, self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_products(self):
        Product.objects.create(**self.product_data)
        url = reverse('products-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




class OrderItemTests(APITestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name="Mwkali", email="mwkali@gmail.com", phone="0724973222")
        self.product = Product.objects.create(
            name="Milking cans",
            category="Dairy Equipment",
            description="Milking cans are commonly used on dairy farms and are essential for maintaining the freshness and hygiene of milk during its journey from the cow to processing or consumption.",
            price="1000.00",
            stock=20,
            supplierid=self.supplier.id,
            product_image_url="https://kenyaagri.com/wp-content/uploads/2024/09/Stainles-milk-cans.jpg"
        )
        self.order = orders.objects.create(order_date="2024-01-01")

        self.data = {
            "order": self.order.id,
            "product": self.product.id,
            "supplier": self.supplier.id,
            "quantity": 2,
            "price": "599.98"
        }

    def test_create_orderItem(self):
        url = reverse('orderItems-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_orderItems(self):
        OrderItem.objects.create(**self.data)
        url = reverse('orderItems-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

