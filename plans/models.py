from django.db import models

# Create your models here.
class Plan(models.Model):
    plan_name = models.CharField(max_length=150)
    plan_discount = models.FloatField()
    rooms_min = models.IntegerField()
    rooms_max = models.IntegerField()
    payment_plan = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Requirement(models.Model):
    requirement_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PlanRequirement(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)