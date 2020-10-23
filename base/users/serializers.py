from rest_framework import serializers
from users.models import Person

# Person serializer
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'