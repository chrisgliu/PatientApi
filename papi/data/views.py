from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .serializers import *
from .models import * 
from django.contrib.auth.models import User
from django.shortcuts import render

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
        queryset = Procedure.objects.all()
        username =  self.kwargs['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        queryset = queryset.filter(patient=user.pk)
        return queryset 

# filtering against a `username` query parameter for a specific procedure id
class InstructionList(generics.ListAPIView):
    serializer_class = InstructionSerializer
    def get_queryset(self):
        queryset = Instruction.objects.all()
        username =  self.kwargs['username']
        program_pk =  self.kwargs['procedure_id']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        try:
            program = Procedure.objects.get(pk=program_pk)
        except Procedure.DoesNotExist:
            raise Http404         
        queryset = queryset.filter(patient=user.pk).filter(program=program.pk)
        return queryset 
    
class ProcedureDetail(APIView):
    # Retrieve, update or delete a Procedure instance.
    def get_object(self, pk):
        try:
            return Procedure.objects.get(pk=pk)
        except Procedure.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        procedure = self.get_object(pk)
        serializer = ProcedureSerializer(procedure, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        procedure = self.get_object(pk)
        serializer = ProcedureSerializer(procedure, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        procedure = self.get_object(pk)
        procedure.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class InstructionDetail(APIView):
    # Retrieve, update or delete an Instruction instance.
    def get_object(self, pk):
        try:
            return Instruction.objects.get(pk=pk)
        except Instruction.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        instruction = self.get_object(pk)
        serializer = InstructionSerializer(instruction, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        instruction = self.get_object(pk)
        serializer = InstructionSerializer(instruction, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instruction = self.get_object(pk)
        instruction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


# Create your views here.
def index(request):
    return render(request, 'index.html');

