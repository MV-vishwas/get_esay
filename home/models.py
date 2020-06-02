from django.db import models
class Member(models.Model):
    id=models.AutoField(primary_key=True)
    F_name=models.CharField(max_length=55)
    L_name=models.CharField(max_length=55)
    mail=models.CharField(max_length=60)
    gender=models.CharField(max_length=10)
    city=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)+" "+self.F_name



class Service(models.Model):
    id=models.AutoField(primary_key=True)
    service_name=models.CharField(max_length=55)
    service_desc=models.CharField(max_length=250)

    def __str__(self):
        return self.service_name




class Service_provider(models.Model):
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=55)
    address=models.CharField(max_length=55)
    mobile_no=models.IntegerField()
    experience=models.CharField(max_length=20)
    charge=models.IntegerField()
    charge_type=models.CharField(max_length=20)
    aadhar_no=models.IntegerField()

    def __str__(self):
        return self.name
