from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer, BillSerializer
from .models import Profile, Bill

@api_view(['GET'])
def apiOverview(req):
    api_urls = {
        'list': '/bills/',
        'Detail View': '/bill-details/<str:pk>/',
        'Create': '/bill-create/',
        'Update': '/bill-update/<str:pk>/',
        'Delete': '/bill-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def billList(req):
    bills = Bill.objects.all()
    serializer = BillSerializer(bills, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def billDetails(req, pk):
    bill = Bill.objects.get(id=pk)
    serializer = BillSerializer(bill, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def billCreate(req):
    serializer = BillSerializer(data=req.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def billUpdate(req, pk):
    bill = Bill.objects.get(id=pk)
    serializer = BillSerializer(instance=bill, data=req.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def billDelete(req, pk):
    bill = Bill.objects.get(id=pk)
    bill.delete()

    return Response('Item  successfully deleted!') 


@api_view(['GET'])
def profileList(req):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def profileDetails(req, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def profileCreate(req):
    serializer = ProfileSerializer(data=req.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def profileUpdate(req, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(instance=profile, data=req.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def profileDelete(req, pk):
    profile = Profile.objects.get(id=pk)
    profile.delete()

    return Response('Item  successfully deleted!') 