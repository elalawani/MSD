from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, UserSerializerProfile, UserUpdateSerializer, UserAddressUpdateSerializer
from .forms import SignupForm


@api_view(['GET'])
def profile(request):
    if not request.user.is_authenticated:
        return Response({'detail': 'Not Authenticated !'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        serializer = UserSerializerProfile(request.user)
        return Response(serializer.data)


@api_view(['PUT'])
def update_profile(request, user_id):
    if not request.user.is_authenticated:
        return Response({'detail': 'Not Authenticated !'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_address(request, user_id):
    if not request.user.is_authenticated:
        return Response({'detail': 'Not Authenticated !'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        serializer = UserAddressUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    form = SignupForm({
        'email': data.get('email'),
        'username': data.get('username'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        form.save()
        return Response({'message': 'success'})

    return Response({'message': 'error', 'errors': form.errors})


@api_view(['GET'])
def doctor_list(request):
    doctors = User.objects.filter(role='DR')
    if not doctors.exists():
        return Response({"detail": "No doctors found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(doctors, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def nurse_list(request):
    nurses = User.objects.filter(role='NR')
    if not nurses.exists():
        return Response({"detail": "No nurses found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(nurses, many=True, context={'request': request})
    return Response(serializer.data)
