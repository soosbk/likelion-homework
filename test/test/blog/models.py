from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=20)
    body=models.TextField(help_text='Enter text')
    create_at=models.DateTimeField(auto_now_add=True) #수정 안돼
    updated_at=models.DateTimeField(auto_now=True)
    publish=models.CharField(default = '', max_length=32)

    def __str__(self):
        return self.title


    