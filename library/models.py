from django.db import models
from django.contrib.auth.models import User
from . import BookStatus,BookAvailablityType
from django.utils.translation import gettext_lazy as _

from django.core.exceptions import ValidationError
  
# creating a validator function
def validate_review(value):
    if value<=10 and value>=1:
        return value
    else:
        raise ValidationError("This field accepts only between 1 to 10")
  


class Book(models.Model):
    
    class AvailibilityType(models.TextChoices):
        AVAILABLE = 'AVAL', _('Available')
        ALLOTED = 'ALTD', _('Alloted')

    class Genre(models.TextChoices):
        FANTASY = 'FNTS', _('Fantasy')
        ROMANCE = 'ROMC', _('Romance')
        COMEDY  = 'CMDY', _('Comedy')
        
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    genre = models.CharField(
        max_length=30,
        choices=Genre.choices,
        default=None,
    )
    availability_type = models.CharField(
        max_length=30,
        choices=AvailibilityType.choices,
        default=AvailibilityType.AVAILABLE,
    )
    rating = models.FloatField(max_length=30,validators=[validate_review],null=True)
    review = models.CharField(max_length=200,null=True)

    def __str__(self) -> str:
       return self.title

    @property
    def is_available(self):
        self.status==BookStatus.AVAILABLE



class Collection(models.Model):
    name = models.CharField(unique=True,max_length=30,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    

class CollectionBook(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,unique=True)
    collection = models.ForeignKey(Collection,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.book.title+ " - " +self.collection.name