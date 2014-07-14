========
MultiSlugRelatedField
========

.. class:: MultiSlugRelatedField(slug_fields[, many, required, queryset])

  Serializer field which may be used to represent the target of a
  relationship using a set of fields on the target.


For example, the following serializer:


.. code-block:: python

    class AddressSerializer(serializers.ModelSerializer):
        postal_code = serializers.SlugRelatedField(many=True, read_only=True,
                                                   slug_fields=('code', 'country'))
        
        class Meta:
            model = Address
            fields = ('street', 'city', 'state', 'postal_code')


Would serialize to a representation like this:


.. code-block:: python
    {
        'street': '123 Main St.',
        'city': 'Boulder',
        'state': 'CO',
        'postal_code': {
            'code': '80305',
            'country': 'USA',
        }
    }

By default this field is read-write, although you can change this behavior
using the ``read_only`` flag.

When using :class:`MultiSlugRelatedField` as a read-write field, you will
normally want to ensure that the slug fields corresponds to a set of model
field declared as ``unique_together``.


---------
Arguments
---------

* ``slug_fields`` - The fields on the target that should be used to represent it.  This should be a set of fields that uniquely identifies any given instance.  For example, ``postal_code', 'country')``.  **required**
* ``many`` - If applied to a to-many relationship, you should set this argument to ``True``.
* ``required`` - If set to ``False`` the field will accept values of ``None`` or the empty-string for nullable relationships.
* ``queryset`` - By default ``ModelSerializer`` classes will use the default queryset for the relationship.  ``Serializer`` classes must either set a queryset explicitly, or set ``read_only=True``.
