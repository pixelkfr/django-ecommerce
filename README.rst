=====
ecommerce
=====

ecommerce is a simple Django project. Users can add, remove or edit orders, initialy imported from an xml file.

Detailed documentation should be in the "docs" directory, but for this little project, there is no specific documentation.

Author: Marie-Charlotte Daureu
Author email: micha.daureu@gmail.com
Python: 2.7.6
Django: 1.8.4

Quick start if you just want to use the app "orders" in another Django project
------------------------------------------------------------------------------

1. Add "orders" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'orders',
    )

2. Include the orders URLconf in your project urls.py like this::

    url(r'^orders/', include('orders.urls')),

3. Run `python manage.py migrate` to create the orders models.

4. Start the development server and visit http://127.0.0.1:8000.
