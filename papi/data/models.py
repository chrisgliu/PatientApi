from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# automatic id primary key fields.

# Default Django User Model:
# username 
# email address 
# first name 
# last name

class Procedure(models.Model):
    procedure_name = models.CharField(max_length=100)
    procedure_date = models.DateTimeField()
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_procedures',
    )

    def __str__(self):
        return f"{self.patient.username}-{self.procedure_name}{self.procedure_date}"

    class Meta:
        verbose_name_plural = "Patient Procedures"

class Instruction(models.Model):
    instruction_msg = models.TextField(max_length=1000, blank=False)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField()
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_instructions',
    )
    program = models.ForeignKey(
        Procedure,
        on_delete=models.CASCADE,
        related_name='procedure_instructions',
    ) 

    def __str__(self):
        return f"{self.patient.username}-{self.program.procedure_name}{self.due_date}"

    class Meta:
        verbose_name_plural = "Patient Instructions"