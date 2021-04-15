from datetime import datetime
from rest_framework import viewsets, mixins
from django.core.exceptions import MultipleObjectsReturned
from .serializers import PollSerializer, QuestionSerializer, VoteSerializer
from .models import Poll, Question, Vote
from .permissions import PollPermission, QuestionPermission


class PollViewSet(viewsets.ModelViewSet):
    """
    REST API для опросов.
    """
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (PollPermission, )


class QuestionViewSet(viewsets.ModelViewSet):
    """
    REST API для вопросов опроса.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (QuestionPermission, )


class VoteViewSet(viewsets.ModelViewSet):
    """
    REST API для голосования в опросе.
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    http_method_names = ('get', 'post')

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            return serializer.save(user=self.request.user)
        return super().perform_create(serializer)

class UserVoteViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Vote.objects.filter(user_id=user_id)
