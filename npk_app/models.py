from django.db import models
from django.contrib.auth.models import User

import numpy as np
from .utils import segment
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO

# Create your models here.
class User_Db(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        #open the image
        pil_img = Image.open(self.image)

        #Convert image to array format
        arr_img = np.array(pil_img)

        #get the segmented image
        img = segment(arr_img)

        #convert back to Image
        seg = Image.fromarray(img)

        buffer = BytesIO()
        seg.save(buffer, format='png')
        seg = buffer.getvalue()

        self.image.save(str(self.image),ContentFile(seg), save=False)

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['created']