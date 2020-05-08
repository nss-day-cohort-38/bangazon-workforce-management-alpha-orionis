from django.db import models
from django.urls import reverse


class EmployeeTrainingProgram(models.Model):
    """
    Creates the join table for the many to many relationship between training programs and employees
    """

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    training_program = models.ForeignKey('TrainingProgram', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Employee_Computer")
        verbose_name_plural = ("Employee_Computers")

    def get_absolute_url(self):
        return reverse("Employee_Training_Program_detail", kwargs={"pk": self.pk})