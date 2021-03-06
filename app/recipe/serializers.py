# from django.contrib.auth import get_user_model, authenticate
# from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from core.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """Serializer for the tag object"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)

#     def create(self, validated_data):
#         """Create a new user with encrypted password and return it"""
#         return get_user_model().objects.create_user(**validated_data)

#     def update(self, instance, validated_data):
#         """Update a user, setting the password correctly and return it"""
#         password = validated_data.pop('password', None)
#         user = super().update(instance, validated_data)

#         if password:
#             user.set_password(password)
#             user.save()

#         return user

class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for the ingredient object"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)


# class AuthTokenSerializer(serializers.Serializer):
#     """Serializer for the user authentication object"""
#     email = serializers.CharField()
#     password = serializers.CharField(
#         style={'input_type': 'password'},
#         trim_whitespace=False
#     )

#     def validate(self, attrs):
#         """Validate and authenticate the user"""
#         email = attrs.get('email')
#         password = attrs.get('password')

#         user = authenticate(
#             request=self.context.get('request'),
#             username=email,
#             password=password
#         )
#         if not user:
#             msg = _('Unable to authenticate with provided credentials')
#             raise serializers.ValidationError(msg, code='authentication')

#         attrs['user'] = user
#         return attrs