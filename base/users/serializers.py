from rest_framework import serializers
from users.models import Person

# Person serializer


class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)

    class Meta:
        model = Person
        fields = ('name',)


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
