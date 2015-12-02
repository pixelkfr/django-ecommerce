from django.db import models

class Order(models.Model):
    marketplace = models.CharField(max_length=100)
    order_purchase_date = models.DateField('purchase date')
    order_amount = models.FloatField()
    order_currency = models.CharField(max_length=3)
    order_id = models.CharField(max_length=19, primary_key=True)

    def __unicode__(self): # __str__ on Python 3
        return self.order_id
