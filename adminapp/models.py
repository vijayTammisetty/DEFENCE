from django.db import models
 
# Create your models here.
class StaffModel(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    empId = models.CharField(max_length=250)
    empDepartment = models.CharField(max_length=250)
    to = models.EmailField(null=True)
    profile= models.ImageField(upload_to='images/',null=True)
    # date_of_birth = models.CharField(max_length=250)
    password = models.CharField(max_length=250,null=True)
    official_email = models.EmailField(null=True)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    pin = models.CharField(max_length=250)
    join_date = models.CharField(max_length=250)
    # releave_date = models.CharField(max_length=250, null=True)


    class Meta:
        db_table = 'staff_details'

    def __str__(self):
        return self.name

    