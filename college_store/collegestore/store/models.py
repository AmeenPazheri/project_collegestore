from django.db import models


class department(models.Model):
    dep_id=models.IntegerField(primary_key=True)
    dep_name=models.CharField(max_length=100)
    dep_img=models.ImageField(upload_to='pics')
    dep_details=models.TextField()

    def __str__(self):
        return self.dep_name

class course(models.Model):
    course_id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=100)
    hod_img=models.ImageField(upload_to='pics')
    course_price=models.DecimalField(max_digits=8, decimal_places=2)
    dep=models.ForeignKey(department,on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


