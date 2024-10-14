from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from election_project.models import Candidate, Voter, MyVotes, Appeal, MyAppeal
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .serializers import CandidateSerializer, VoterSerializer, MyVotesSerializer, AppealSerializer, MyAppealSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class VoterViewSet(viewsets.ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class MyVotesViewSet(viewsets.ModelViewSet):
    queryset = MyVotes.objects.all()
    serializer_class = MyVotesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class AppealListView(viewsets.ModelViewSet):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer


class MyAppealListView(viewsets.ModelViewSet):
    queryset = MyAppeal.objects.all()
    serializer_class = MyAppealSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MyAppeal.objects.filter(user=self.request.user)


