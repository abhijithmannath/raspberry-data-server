from django.utils import timezone
from rest_framework import serializers
class CustomDateTimeField(serializers.DateTimeField):
    def to_representation(self, value):
        tz = timezone.get_default_timezone()
        # timezone.localtime() defaults to the current tz, you only
        # need the `tz` arg if the current tz != default tz
        value = timezone.localtime(value, timezone=tz)
        # py3 notation below, for py2 do:
        return super((CustomDateTimeField, self).to_representation(value)
