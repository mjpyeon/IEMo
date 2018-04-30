from django.db import models

# Create your models here.
class Image(models.Model):
    file_name = models.CharField(max_length=100, default='default.jpg')
    image = models.ImageField(upload_to='%Y/%m/%d')
    content = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Image, self).delete(*args, **kwargs)