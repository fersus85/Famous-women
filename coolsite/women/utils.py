from django.db.models import Count

from .models import *


class DataMixin:

    def get_user_context(self, **kwargs):

        context = kwargs
        return context