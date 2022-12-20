from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from shop.models import Customer, Order


class HomePageView(TemplateView):
    template_name = 'home.html'


class CustomersListView(ListView):
    template_name = 'customers.html'
    model = Customer
    context_object_name = 'customers_list'


class OrdersListView(ListView):
    template_name = 'orders.html'
    model = Order
    context_object_name = 'orders_list'


class SearchView(ListView):
    template_name = "search.html"
    model = Order
    context_object_name = 'orders_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Order.objects.filter(
            Q(customer__first_name__icontains=query) | Q(customer__last_name__icontains=query)
        ).order_by('order_date').reverse()
