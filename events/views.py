from django.shortcuts import render
from .serializers import LeadSerializer
from rest_framework import generics
from .models import Events


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = LeadSerializer
