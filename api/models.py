from django.db import models


class Shipment(models.Model):
    """ Model describe Shipment model """

    name = models.CharField(verbose_name='Name Of Shipment', max_length=100,)
    description = models.CharField(verbose_name='Description Of Shipment', max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='Amount')
    price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='Price of Shipment')

    def __str__(self):
        return f'{self.name} | {self.description}'
