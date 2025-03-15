from rest_framework import serializers
from blog.models import Post


class PostSerializers(serializers.ModelSerializer):

    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created",
            'status',
            'slug',
        )
        model = Post


