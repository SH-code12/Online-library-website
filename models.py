from django.db import models
from django.contrib.auth.hashers import make_password, check_password



# Create your models here.


class Books(models.Model):
    

    listCategory = [
        ('Programming','Programming'),
        ('Trend','Trend'),
        ('Science Fiction','Science Fiction'),
        ('Travel','Travel'),
    ]
    listStatus = [
        ('Borrow','Borrow'),
        ('Borrowed','Borrowed'),
        ('Not In Library','Not In Library'),
        ('Read Only','Read Only'),
    ]
    image = models.ImageField(upload_to='Photos/%y/%m/%d')
    name = models.CharField(max_length = 80, verbose_name = 'Title')
    author = models.CharField(max_length = 100)
    category = models.CharField(max_length=50 ,choices=listCategory)
    description = models.TextField()
    status = models.CharField(max_length=50 ,choices=listStatus)
    
    
    def __str__(self):
        return self.name
    
    
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    confirmPassword = models.CharField(max_length=8)
    email = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=True)

    
    def __str__(self):
        return self.username
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()
        
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def is_admin_user(self):
        return self.is_admin
