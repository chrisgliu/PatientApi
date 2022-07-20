from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import generics
from .serializers import *
from .models import * 
from django.contrib.auth.models import User

# ViewSets define the view behavior.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

class InstructionViewSet(viewsets.ModelViewSet):
    queryset = Instruction.objects.all()
    serializer_class = InstructionSerializer

# filtering against a `username` query parameter
class ProcedureList(generics.ListAPIView):
    serializer_class = ProcedureSerializer
    def get_queryset(self):
        queryset =  Procedure.objects.none()
        username =  self.kwargs['username']
        if username is None: 
            return queryset
        user = User.objects.get(username=username)
        if user is None: 
            return queryset 
        queryset = Procedure.objects.all()
        queryset = queryset.filter(patient=user.pk)
        return queryset  

class InstructionList(generics.ListAPIView):
    serializer_class = InstructionSerializer
    def get_queryset(self):
        queryset =  Procedure.objects.none()
        username =  self.kwargs['username']
        if username is None: 
            return queryset
        program_pk =  self.kwargs['program_id']
        if  program_pk is None: 
            return queryset
        user = User.objects.get(username=username)
        if user is None: 
            return queryset 
        program = Procedure.objects.get(pk=program_pk)
        if user is None: 
            return queryset 
        queryset = Instruction.objects.all()
        queryset = queryset.filter(patient=user.pk).filter(program=program.pk)
        return queryset 


# Create your views here.
def index(request):
    return HttpResponse("Created By Chris")

