from django.db import models


class Customer(models.Model):

    first_name = models.CharField(max_length= 70)
    last_name = models.CharField(max_length= 70)
    age = models.IntegerField()
    email = models.EmailField(max_length=60, unique=True)
    address = models.TextField(max_length=200)
    contact = models.BigIntegerField()


    class Meta:
        db_table = 'CUSTOMER_MASTER'


    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)


