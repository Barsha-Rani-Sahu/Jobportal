from django.db import models 



class Category(models.Model):
    Category_name=models.CharField(max_length=50,primary_key=True)

    class Meta:
        db_table='Category'

    def __str__(self):
        return self.Category_name
