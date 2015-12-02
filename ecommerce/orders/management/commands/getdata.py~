import urllib2
import logging
import xml.etree.ElementTree as ET

from django.core.management.base import BaseCommand, CommandError
from django.core import serializers

from orders.models import Order


class Command(BaseCommand):
    """
        Simple command to extract data from xml file and save them in the Order model.
        Data are available at the following adress: http://test.ecommerce.io/orders-test.xml
    """
    help = 'Load data from xml file, and save them in the Order model'

    def handle(self, *args, **options):
        logger = logging.getLogger()
        steam_handler = logging.StreamHandler()
        steam_handler.setLevel(logging.DEBUG)
        logger.addHandler(steam_handler)
        try:
            request = urllib2.urlopen("http://test.ecommerce.io/orders-test.xml")
            tree = ET.parse(request)
        except:
            raise CommandError('Xml file is not valid')

        orders = tree.find("orders")
        for item in orders.getiterator('order'):
            if ((item.find('marketplace').text) is not None)\
                 and(item.find('order_purchase_date').text is not None)\
                 and(item.find('order_amount').text is not None)\
                 and(item.find('order_currency').text is not None)\
                 and(item.find('order_id').text is not None):
                marketplace = item.find('marketplace')
                order_purchase_date = item.find('order_purchase_date')
                order_amount = item.find('order_amount')
                order_currency = item.find('order_currency')
                order_id = item.find('order_id')
                # add and save a new order
                new_order = Order(marketplace=marketplace.text,
                                  order_purchase_date=order_purchase_date.text,
                                  order_amount=order_amount.text,
                                  order_currency=order_currency.text,
                                  order_id=order_id.text)
                new_order.save()
            else:
                logger.warning("A required argument is missing"
                              " for one order, please look at your xml file.")
