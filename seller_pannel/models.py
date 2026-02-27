from django.db import models

class Order(models.Model):
    product_name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="Almost Delivered")

    def __str__(self):
        return f"{self.product_name} - {self.customer_name}"