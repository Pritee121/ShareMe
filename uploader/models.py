# from django.db import models
# import uuid

# class UploadedFile(models.Model):
#     file = models.FileField(upload_to='uploads/')
#     code = models.CharField(max_length=8, unique=True, editable=False)
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         if not self.code:
#             self.code = uuid.uuid4().hex[:8]
#         super().save(*args, **kwargs)
from django.db import models
import random
import string

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    code = models.CharField(max_length=8, unique=True, editable=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(random.choices(string.digits, k=4))
        super().save(*args, **kwargs)
