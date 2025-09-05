from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
def validate_file_type(file):
    valid_mime_types = [
        'application/pdf',  # PDF
        'image/jpeg',       # JPG/JPEG
        'image/png',        # PNG
        'image/gif',        # GIF
    ]
    if file.content_type not in valid_mime_types:
        raise ValidationError('Unsupported file type. Only PDF and images are allowed.')
    
    
class distributer(models.Model):
    
    name = models.CharField(max_length=100)
    eamil= models.EmailField(max_length=254, unique=True)
    pasward= models.CharField(max_length=100)
    # partner_code = 
    adhar_card = models.FileField(upload_to='uploads/', validators=[validate_file_type])
    pan_card = models.FileField(upload_to='uploads/', validators=[validate_file_type])
    photo = models.FileField(upload_to='uploads/', validators=[validate_file_type])
    
