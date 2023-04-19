from django.db import models
# Create your models here.

# Model users


class Users(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superUser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['username', 'id']
    
    def __str__(Users):
        return Users.username

        
# Model rol


class Role(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)

# ModelRolUser


class RoleUser(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
