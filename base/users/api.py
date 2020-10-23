from users.models import Person
from rest_framework.response import Response
from users.serializers import PersonSerializer, FriendsSerializer
from .utils import recommend_by_number_of_common_friends
from rest_framework.decorators import action
from rest_framework.generics import UpdateAPIView
from rest_framework import viewsets


# Person Viewset


class PersonViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing all persons in the database.

    And a recommendation method tha retrieves a recommendation for a person.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @action(detail=True, methods=['get'])
    def recommendation(self, request, pk):
        recommendation = recommend_by_number_of_common_friends(pk)
        serializer_class = PersonSerializer(recommendation, many=True)
        return Response(serializer_class.data)


class FriendsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing friends of a person.
    """
    queryset = Person.objects.all()
    serializer_class = FriendsSerializer


class UpdateFriends(UpdateAPIView):
    """
    A simple ViewSet for updatign the list of friends of a person.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
