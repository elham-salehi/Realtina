from datetime import datetime

from reservations.models import List


def calculate_bookable_rooms(check_in: datetime, check_out: datetime, list: List):
    # Find conflicting reservations within the specified time range
    conflicting_reservations = list.reservations.filter(
        check_in__lt=check_out,
        check_out__gt=check_in,
    )

    # Calculate the total number of rooms booked in the conflicting reservations
    total_booked = sum([reserve.booked_rooms for reserve in conflicting_reservations])
    # Calculate the number of bookable rooms
    bookable_rooms = list.rooms_count - total_booked
    return bookable_rooms
