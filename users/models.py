from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

    
class IMUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(
        max_length=50, 
        choices = {
        'EIT': 'EIT',  # Actual value: 'EIT', Human-readable name: 'EIT'
        'TEACHING_FELLOW': 'Teaching Fellow',
        'ADMIN_STAFF': 'Admin Staff',
        'ADMIN': 'Admin'
        }, 
        default = 'EIT'
        )
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True )

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
    
class Cohort(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    year = models.PositiveIntegerField
    start_date = models.DateTimeField (blank=True, null=True)
    end_date = models.DateTimeField (blank=True, null=True)
    is_active = models.BooleanField (default=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True )
    date_modified = models.DateTimeField(auto_now=True,  blank = True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_cohorts')

    def __str__(self):
        return f"{self.name}"


class CohorMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='members')
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohorts')
    is_active = models.BooleanField (default=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True,  blank = True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='added_cohort_members')

    def __str__(self):
        return f"{self.member}, {self.cohort}"