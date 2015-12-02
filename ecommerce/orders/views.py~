from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Q

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

from .serializers import OrderSerializer
from .models import Order
from .forms import OrderForm


class IndexView(generic.ListView):
    """
    A simple view to list all orders, or filter by attribute.
    """
    template_name = 'orders/index.html'
    context_object_name = 'latest_order_list'

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search :
            return Order.objects.filter(
                Q(marketplace__contains = search)
                | Q(order_id__contains = search)
                | Q(order_amount__contains = search)
                | Q(order_currency__contains = search)
                | Q(order_purchase_date__contains = search)
                )
        else :
            return Order.objects.all()


class DetailView(generic.DetailView):
    """
    A simple view to see details of an order.
    """
    model = Order
    template_name = 'orders/detail.html'


class OrderViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing order instances, with the rest Framework.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)


def order_new(request):
    """
    A simple view to add a new order.
    """
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('orders:detail', pk=order.order_id)
    else:
        form = OrderForm()
    return render(request, 'orders/order_edit.html', {'form': form})


def order_remove(request, pk):
    """
    A simple view to remove an order.
    """
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('orders:index')


def order_edit(request, pk):
    """
    A simple view to edit an order.
    """
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            return redirect('orders:detail', pk=order.order_id)
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_edit.html', {'form': form})
