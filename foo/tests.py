from django.test import TestCase

from foo.models import Place, Restaurant


class BugOneToOne(TestCase):
    def test_bug_one_to_one(self):
        place = Place.objects.create(name="Bob's Cafe", address="123 Main St")
        restaurant = Restaurant.objects.create(serves_hot_dogs=True, serves_pizza=False)

        place.restaurant = restaurant
        place.save()

        place.refresh_from_db()

        self.assertEqual(place.restaurant, restaurant)
