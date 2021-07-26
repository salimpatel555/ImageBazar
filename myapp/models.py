from django.db import models

# Create your models here.

class Category(models.Model):
    title= models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title
         

class Image(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='images/')
    added_date=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)    
 
   
        
   
    # @staticmethod
    # def get_all_product_by_id(category_id):
    #     if category_id:
    #         return Image.objects.filter(category=category_id)
    #     else:
    #         Image.objects.all()             