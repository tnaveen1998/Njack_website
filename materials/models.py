from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_pic = models.CharField(max_length=1000)

    def __str__(self):
        return (self.category_name)

class Resource(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=100)
    material_description = models.CharField(max_length=5000)
    author = models.CharField(max_length=100)
    post_date = models.CharField(max_length=20)
    content = models.CharField(max_length=10000000)

    def __str__(self):
        return (self.material_name + ' - ' + self.category.category_name)
