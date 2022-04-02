from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class Teachers(models.Model):
    id = models.AutoField(primary_key=True)
    first_name =models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    email =models.EmailField()
    username =models.CharField(max_length=255, unique=True)
    address =models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.admin}'

class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (2, "Teacher"))
    id = models.AutoField(primary_key=True)
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.admin}'


class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
	    return self.class_name


class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subject_name}'


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField(blank=True)
    address = models.TextField()
    class_id = models.ForeignKey(Classes, on_delete=models.DO_NOTHING, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.admin}'


class TeacherMapping(models.Model):
    id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE, default=1)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)



