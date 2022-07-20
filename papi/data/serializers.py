from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'first_name', 'last_name', 'is_staff']

class ProcedureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Procedure
        fields = ['id', 'url', 'procedure_name', 'procedure_date', 'patient']

class InstructionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instruction
        fields = ['id', 'url', 'instruction_msg', 'completed', 'due_date', 'patient', 'program']
