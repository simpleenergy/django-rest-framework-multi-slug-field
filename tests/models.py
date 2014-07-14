from django.db import models


class TimeZone(models.Model):
    pass


class PostalCode(models.Model):
    code = models.CharField(max_length=10)
    country = models.CharField(max_length=5)

    timezone = models.ForeignKey(TimeZone, null=True, blank=True,
                                 related_name='postal_codes')

    class Meta:
        unique_together = (
            ('code', 'country'),
        )


class Address(models.Model):
    postal_code = models.ForeignKey(PostalCode, null=True, blank=True)
