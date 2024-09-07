from django.db import models

# Create your models here.
class departments(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_desc = models.TextField()
    def __str__(self):
        return self.dept_name
class doctor(models.Model):
    doct_name = models.CharField(max_length=225)
    doct_spec = models.CharField(max_length=225)
    doct_dept = models.ForeignKey(departments,on_delete=models.CASCADE)
    doct_image = models.ImageField(upload_to='doctors')
    def __str__(self):
        return self.doct_name + " " + self.doct_spec
class booking(models.Model):
    p_name = models.CharField(max_length=225)
    p_phone = models.CharField(max_length=225)
    p_email = models.CharField(max_length=225)
    doct_name =models.ForeignKey(doctor,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True) 
