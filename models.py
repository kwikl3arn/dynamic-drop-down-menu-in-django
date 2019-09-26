from django.db import models


# Create your models here.
class main_menu(models.Model):
    m_menu_id = models.AutoField(primary_key=True)
    m_menu_name = models.CharField(max_length=50)
    m_menu_link = models.CharField(max_length=100)


class sub_menu(models.Model):
    s_menu_id = models.AutoField(primary_key=True)
    m_menu_id = models.IntegerField()
    s_menu_name = models.CharField(max_length=50)
    s_menu_link = models.CharField(max_length=100)

