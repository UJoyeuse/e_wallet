from django.db import models
from django.contrib.auth.models import AbstractUser

class Client(AbstractUser):
    phone_number=models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    dob = models.DateTimeField()
      
    class Meta:
     db_table = 'client'

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    
class Account(models.Model):
    owner = models.OneToOneField( Client, on_delete=models.CASCADE, null=False)       
    account_no=models.CharField(max_length=100,primary_key=True,unique=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_date=models.DateTimeField(auto_now=True)
    balance=models.IntegerField(default=1000)

    class Meta:
     db_table = 'account'

    def __str__(self):
        return self.account_no

class Transaction(models.Model):
    amount=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    account_sender = models.ForeignKey(Account,related_name='sender_account',on_delete=models.CASCADE)
    account_receiver = models.ForeignKey(Account,related_name='receiver_account',on_delete=models.CASCADE)

    class Meta:
     db_table = 'transaction'

    def __str__(self):
        return self.amount

