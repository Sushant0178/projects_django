from django.db import models





class Product(models.Model):
    product_id   = models.AutoField
    product_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    pub_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.product_name
    





