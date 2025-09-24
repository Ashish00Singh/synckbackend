from django.db import models
import random
import string
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
# Create your models here.
def validate_file_type(file):
    valid_mime_types = [
        'application/pdf',  
        'image/jpeg',
        'image/png',
        'image/gif',
    ]
    if file.content_type not in valid_mime_types:
        raise ValidationError('Unsupported file type. Only PDF and images are allowed.')
    
class distributer(models.Model):

    name = models.CharField(max_length=100)
    eamil= models.EmailField(max_length=254, unique=True)
    phone= models.IntegerField( blank=True )
    address= models.CharField(max_length=250)
    date_of_bearth=models.DateField( null=True )
    
    adhar_number = models.CharField(
    max_length=16,
    unique=True,
    validators=[RegexValidator(r'^\d{16}$', 'Aadhar number must be 16 digits')],
    default="1234567890123456")
    insurnce_number=models.CharField(max_length=80, null=True)
    insurnce_expiry_date=models.DateField()
    area_of_specialization= models.CharField(max_length=80)
    preferred_sale_area= models.CharField(max_length=120, null=True)
    bank_name=models.CharField(max_length=80)
    account_type=models.CharField(max_length=80)
    ifsc_code=models.CharField(max_length=50)
    bank_account = models.IntegerField(null=True)
    pan_number = models.CharField(max_length=50)
    partner_code= models.CharField(max_length=100, unique=True, blank=True )
    bank_imag = models.FileField(upload_to='uploads/', validators=[validate_file_type])
    adhar_card = models.FileField(upload_to='uploads/', validators=[validate_file_type])
    pan_card = models.FileField(upload_to='uploads/', validators=[validate_file_type])
    photo = models.FileField(upload_to='uploads/', validators=[validate_file_type])
    terms_accepted = models.BooleanField(default=False)
     
    def save(self, *args, **kwargs):

        # ✅ generate partner_code if not already set
        if not self.partner_code:
            part1 = self.name[:2].upper() if self.name else "XX"
            part2 = str(self.adhar_number)[:2] if self.adhar_number else "00"
            part3 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))
            self.partner_code = f"{part1}{part2}{part3}"

        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.name