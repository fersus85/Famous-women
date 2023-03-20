from rest_framework import serializers

from women.models import *


class WomenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Women
        fields = ('id', 'title', 'content', 'cat_id')
