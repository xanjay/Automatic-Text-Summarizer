from django.db import models
from .validators import validate_file_extension
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Document(models.Model):
    summary_p = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(50)])
    document = models.FileField(validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
