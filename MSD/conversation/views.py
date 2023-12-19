from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Conversation, ConversationMessage
from .serializers import ConversationSerializer, ConversationMessageSerializer, OnlyConversationSerializer


@api_view(['GET'])
def get_conversation(request, patient_id):
    try:
        conversation = Conversation.objects.get(patient__id=patient_id)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Conversation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_conversations(request):
    try:
        conversation = Conversation.objects.filter(users=request.user)
        serializer = OnlyConversationSerializer(conversation, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Conversation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_message(request, conversation_id):
    user = request.user
    conversation = Conversation.objects.get(id=conversation_id)

    # Check if the user is part of the conversation
    if user not in conversation.users.all():
        return Response({"message": "You are not part of this conversation"}, status=400)

    data = request.data.copy()
    data["conversation"] = str(conversation_id)

    serializer = ConversationMessageSerializer(data=data)

    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_messages(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)

    if request.user not in conversation.users.all():
        return Response({"message": "You are not part of this conversation"}, status=400)

    messages = conversation.message.all()
    serializer = ConversationMessageSerializer(messages, many=True)

    return Response(serializer.data)


@api_view(['PUT'])
def update_message(request, message_id):
    message = get_object_or_404(ConversationMessage, id=message_id)

    # Check if the user is the author of the message
    if request.user != message.user:
        return Response({"message": "You can only update your own messages"}, status=403)

    serializer = ConversationMessageSerializer(message, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)

    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_message(request, message_id):
    message = get_object_or_404(ConversationMessage, id=message_id)

    # Check if the user is the author of the message
    if request.user != message.user:
        return Response({"message": "You can only delete your own messages"}, status=403)

    message.delete()
    return Response({"message": "Message deleted"}, status=204)
