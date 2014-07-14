import collections

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import ugettext_lazy as _

from rest_framework.relations import RelatedField


class MultiSlugRelatedField(RelatedField):
    """
    Represents a relationship using a unique set of fields on the target.
    """
    read_only = False

    default_error_messages = {
        'does_not_exist': _("Object with %s does not exist."),
        'invalid': _('Invalid value.'),
    }

    def __init__(self, *args, **kwargs):
        self.slug_fields = kwargs.pop('slug_fields', None)
        assert self.slug_fields, "slug_fields is required"
        super(MultiSlugRelatedField, self).__init__(*args, **kwargs)

    def to_native(self, obj):
        return dict(zip(
            self.slug_fields,
            (getattr(obj, slug_field) for slug_field in self.slug_fields),
        ))

    def from_native(self, data):
        if self.queryset is None:
            raise Exception('Writable related fields must include a `queryset` argument')

        if not isinstance(data, collections.Mapping):
            raise ValidationError(self.error_messages['invalid'])

        if not set(data.keys()) == set(self.slug_fields):
            raise ValidationError(self.error_messages['invalid'])

        try:
            return self.queryset.get(**data)
        except ObjectDoesNotExist:
            lookups = ['='.join((lookup, value)) for lookup, value in zip(self.slug_fields, data)]
            raise ValidationError(self.error_messages['does_not_exist'] %
                                  ' '.join(lookups))
        except (TypeError, ValueError):
            msg = self.error_messages['invalid']
            raise ValidationError(msg)
