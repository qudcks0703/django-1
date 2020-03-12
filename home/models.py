from django.db import models

# Create your models here.
class Member(models.Model):
    myid=models.CharField(max_length=50,blank=False,primary_key=True)
    pw=models.CharField(max_length=50,blank=False)
    name=models.CharField(max_length=50)
    reg=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.myid+"님의 아이디"
