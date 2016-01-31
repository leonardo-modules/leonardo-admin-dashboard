
=================================
Leonardo leonardo-admin-dashboard
=================================

Admin dashboard for Leonardo CMS built on django-jet. Support custom menu and easy extending with auto registering of new widgets.

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo-admin-dashboard

Configuration
-------------

This module requires ``dashboard_menu`` item in ``LEONARDO_CONF_SPEC``::

    LEONARDO_CONF_SPEC = {
        'dashboard_menu': []
    }

Optionaly you can add dashboard widgets::

    LEONARDO_CONF_SPEC = {
        'dashboard_widgets_available': [],
        'dashboard_widgets': []
    }

Usage
-----

Add your menu items into ``dashboard_menu`` array as string path to your menu::

    dashboard_menu = ['leonardo_store.menu.store_menu']

For menu items use modules from ``leonardo_admin_dashboard.modules``::

    from leonardo_admin_dashboard import modules

    store_menu = modules.SubMenuLinkList(
        _('Store'),
        children=[{
                    'title': 'Catalogue',
                    'url': reverse('catalogue'),
                    'external': False,
                    'icon': 'icon-book'
                    }],
    )

For more examples see ``menu.py`` or visit ``django-admin-tools`` and ``django-jet`` documentations.

Read More
=========

* https://github.com/django-leonardo/django-leonardo
* https://github.com/geex-arts/django-jet