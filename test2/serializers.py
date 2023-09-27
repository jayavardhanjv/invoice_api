from rest_framework import serializers
from .models import Invoice, Invoice_Detail



class InvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice_Detail
        fields='__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    # details = InvoiceDetailsSerializer(many=True, read_only=True)
    class Meta:
        model=Invoice
        fields='__all__'