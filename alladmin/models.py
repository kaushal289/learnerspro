from django.db import models

# Create your models here.
class Admin(models.Model):
    admin_id=models.AutoField(auto_created=True, primary_key=True)
    admin_username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    class Meta:
        db_table="admin"