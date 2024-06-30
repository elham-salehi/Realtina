from django.db import models


# List model to represent different lists
class List(models.Model):
    name = models.CharField(max_length=150, unique=True)
    rooms_count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.rooms_count} rooms"

    class Meta:
        verbose_name = 'List'
        verbose_name_plural = 'Lists'


# Reservation model to represent reservations for lists
class Reservation(models.Model):
    list = models.ForeignKey(List, related_name='reservations', on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=150)
    booked_rooms = models.PositiveIntegerField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f"{self.guest_name} - {self.list.name} ({self.booked_rooms} rooms, from {self.check_in}" \
               f" to {self.check_out})"

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
