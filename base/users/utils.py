from users.models import Person


def friends(name):
    """Returns a set of the friends of the given user, in the given graph.
    """
    friends_list = Person.objects.get(name=name).friends.all()
    return set(friends_list)


def friends_of_friends(user):
    """Returns a set of friends of friends of the given user, in the given graph.
    The result does not include the given user nor any of that user's friends.
    """
    friends_list = friends(user)
    result_set = set()
    for friend in friends_list:
        result_set.update(friends(friend))

    friends_list.add(user)

    result_set = result_set.difference(friends_list)

    return result_set


def common_friends(user1, user2):
    """Returns the set of friends that user1 and user2 have in common."""
    result_set = friends(user1).intersection(friends(user2))
    return result_set


def number_of_common_friends_map(user):
    """Returns a map from each user U to the number of friends U has in common
    with the given user.
    The map keys are the users who have at least one friend in common with the
    given user, and are neither the given user nor one of the given user's
    friends.
    Take a graph G for example:
        - A and B have two friends in common
        - A and C have one friend in common
        - A and D have one friend in common
        - A and E have no friends in common
        - A is friends with D
    number_of_common_friends_map(G, "A")  =>   { 'B':2, 'C':1 }
    """
    common_friends_map = {}
    user_friends = friends_of_friends(user)

    for friend in user_friends:
        length = len(common_friends(user, friend))
        if length >= 1:
            common_friends_map[friend] = length

    return common_friends_map


def number_map_to_sorted_list(map):
    """Given a map whose values are numbers, return a list of the keys.
    The keys are sorted by the number they map to, from greatest to least.
    When two keys map to the same number, the keys are sorted by their
    natural sort order, from least to greatest."""

    return [v[0] for v in sorted(map.items(), key=lambda kv: (-kv[1], kv[0]))]


def recommend_by_number_of_common_friends(user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names of people in the graph
    who are not yet a friend of the given user.
    The order of the list is determined by the number of common friends.
    """
    number_of_common_friends_dict = number_of_common_friends_map(user)

    sorted_recommend_key = number_map_to_sorted_list(
        number_of_common_friends_dict)

    return sorted_recommend_key
