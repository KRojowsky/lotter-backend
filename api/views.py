from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Member
from .serializer import MemberSerializer
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_members(request):
    members = Member.objects.all()
    serializedData = MemberSerializer(members, many=True).data
    return Response(serializedData)


@api_view(['POST'])
def create_member(request):
    data = request.data
    serializer = MemberSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        logger.error(f"Validation errors: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def check_member_status(request):
    phone = request.data.get('phone')
    receipt = request.data.get('receipt')

    if not phone or not receipt:
        return Response({'error': 'Wymagany numer telefonu i numer paragonu'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        member = Member.objects.get(phone=phone, receipt=receipt)
        return Response({'exists': True}, status=status.HTTP_200_OK)
    except Member.DoesNotExist:
        return Response({'exists': False}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return Response({'error': 'Wystąpił nieoczekiwany błąd.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

