from django.db import models

class Invoice(models.Model):
    CustomerName=models.CharField(max_length=122)
    Date=models.DateField()
    def __str__(self):
        return self.CustomerName

class  Invoice_Detail(models.Model):
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    description=models.CharField(max_length=122)
    quantity=models.IntegerField()
    unit_price=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
         return self.description
