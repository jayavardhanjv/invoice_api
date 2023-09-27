# from rest_framework import request
from django.http import JsonResponse
from .models import Invoice , Invoice_Detail
from .serializers import InvoiceSerializer , InvoiceDetailsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def invoice_list(request):
    if request.method == 'GET':
        invoise= Invoice.objects.all()
        serializer=InvoiceSerializer(invoise, many=True)
        return Response(serializer.data)
    

@api_view(['GET','POST'])
def invoice_details(request):
    if request.method == 'GET':
        invoise= Invoice_Detail.objects.all()
        serializer=InvoiceDetailsSerializer(invoise, many=True)
        return Response(serializer.data)


@api_view(['GET','DELETE','PUT'])
def invoice_change(request,id,format=None):
    try:
        invoice=Invoice.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=InvoiceSerializer(invoice)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer=InvoiceSerializer(invoice,data=request.data)
        if serializer.valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','DELETE','PUT'])
def invoice_details_change(request,id,format=None):
    try:
        invoice=Invoice_Detail.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=InvoiceDetailsSerializer(invoice)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer=InvoiceDetailsSerializer(invoice,data=request.data)
        if serializer.valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)