from rest_framework import routers, serializers, viewsets

from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('marketplace', 'order_purchase_date',
                'order_amount', 'order_currency', 'order_id')
