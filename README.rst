=============================
django-rest-framework-multi-slug-field
=============================

.. image:: https://badge.fury.io/py/django-rest-framework-multi-slug-field.png
    :target: https://badge.fury.io/py/django-rest-framework-multi-slug-field

.. image:: https://travis-ci.org/pipermerriam/django-rest-framework-multi-slug-field.png?branch=master
    :target: https://travis-ci.org/pipermerriam/django-rest-framework-multi-slug-field

.. image:: https://coveralls.io/repos/pipermerriam/django-rest-framework-multi-slug-field/badge.png?branch=master
    :target: https://coveralls.io/r/pipermerriam/django-rest-framework-multi-slug-field?branch=master

A field for representing a relationship via multiple fields on the target

Documentation
-------------

The full documentation is at https://django-rest-framework-multi-slug-field.readthedocs.org.

Quickstart
----------

Install django-rest-framework-multi-slug-field::

    pip install django-rest-framework-multi-slug-field

Then use it in a project::

    from rest_framework_msf import MultiSlugField

Features
--------

* :class:`~rest_framework_msf.fields.MultiSlugField` - Serializer field for
  representing a relationship via a set of fields on the target.
