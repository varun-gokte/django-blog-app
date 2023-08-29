from django.db import models
from django.contrib import admin

# Create your models here.
class Blog_Post(models.Model):
    user_name = models.CharField(max_length=122)
    title = models.CharField(max_length=122, default="")
    post_content = models.TextField()
    date = models.DateTimeField()

    def __str__(self) -> str:
        return "Title: "+self.title
    
class Comments(models.Model):
    user_name = models.CharField(max_length=122)
    comment = models.TextField()
    art_id = models.ForeignKey(Blog_Post, on_delete=models.CASCADE)


class Blog_PostAdmin(admin.ModelAdmin):
    fields= ['user_name', 'title','post_content','date']