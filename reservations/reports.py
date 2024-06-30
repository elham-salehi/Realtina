import logging

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from reservations.models import List

logger = logging.getLogger(__name__)


def report(request):
    try:
        lists = List.objects.all()
        reports = []

        for list in lists:
            reservations = list.reservations.all()
            reports.append({
                'List': list,
                'reservations': reservations
            })
        # Generate report in HTML format
        return render(request, 'report.html', {'reports': reports})
    except ValueError as e:
        logger.exception(e)
        return Response('Value error', status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.exception(e)
        return Response('Server error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
