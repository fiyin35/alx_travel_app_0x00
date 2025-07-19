from rest_framework import serializers
from .models import Listing, Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'customer_name', 'check_in', 'check_out', 'created_at']

class ListingSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Listing
        fields = ['id', 'name', 'description', 'location', 'price_per_night', 'available', 'created_at', 'bookings']


