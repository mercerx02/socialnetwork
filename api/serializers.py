from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Post

import services as likes_services

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner','is_fan','total_likes']

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` твит (`obj`).
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)

User = get_user_model()

class FanSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
        )

    def get_full_name(self, obj):
        return obj.get_full_name()