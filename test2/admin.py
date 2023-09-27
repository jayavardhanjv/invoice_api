from django.contrib import admin
from .models import Invoice
from .models import Invoice_Detail

admin.site.register(Invoice)
admin.site.register(Invoice_Detail)