import logging

from django.utils.dateparse import parse_datetime
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import List, Reservation
from .serializers import ListSerializer, ReservationSerializer
from .utils import calculate_bookable_rooms

logger = logging.getLogger(__name__)


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    @action(detail=True, methods=['get'])
    def bookable(self, request, pk=None):
        try:
            list = self.get_object()
            check_in = request.query_params.get('check_in')
            check_out = request.query_params.get('check_out')
            required_rooms = int(request.query_params.get('rooms', 1))

            if not check_in or not check_out:
                return Response({'error': 'Check in time and check out time are required'},
                                status=status.HTTP_400_BAD_REQUEST)

            # Parse the check_in and check_out from string to datetime
            check_in = parse_datetime(check_in)
            check_out = parse_datetime(check_out)
            bookable_rooms = calculate_bookable_rooms(check_in, check_out, list)

            # Check if the required number of rooms are available
            if bookable_rooms >= required_rooms:
                return Response({'is_bookable': True}, status=status.HTTP_200_OK)
            else:
                return Response({'is_bookable': False}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            logger.exception(e)
            return Response('Value error', status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(e)
            return Response('Server error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            list = serializer.validated_data['list']
            check_in = serializer.validated_data['check_in']
            check_out = serializer.validated_data['check_out']
            booked_rooms = serializer.validated_data['booked_rooms']
            if check_out < check_in:
                return Response({"check out time can't be before check in time"},
                                status=status.HTTP_400_BAD_REQUEST)

            bookable_rooms = calculate_bookable_rooms(check_in, check_out, list)

            if booked_rooms > bookable_rooms:
                return Response({'Not enough rooms available'}, status=status.HTTP_400_BAD_REQUEST)

            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.exception(e)
            return Response('Server error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
