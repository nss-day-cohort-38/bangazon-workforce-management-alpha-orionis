from django.db import models
from django.urls import reverse


class EmployeeComputer(models.Model):
    """
    Creates the join table for the many to many relationship between computers and employees
    Author: Joe Shep
    methods: none
    """

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    computer = models.ForeignKey('Computer', on_delete=models.CASCADE)
    assign_date = models.DateField(null=False)
    unassign_date = models.DateField(null=True, blank=True, default=None)

    # class Meta:
    #     verbose_name = ("Employee_Computer")
    #     verbose_name_plural = ("Employee_Computers")

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})
