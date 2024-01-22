from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer, BillSerializer
from .models import Profile, Bill
from .supabase_utils import send_magic_link

@api_view(['GET'])
def apiOverview(req):
    api_urls = {
        'list': reverse('bill_list'),
        'Detail View': reverse('bill_details', args=['<str:pk>']),
        'Create': reverse('bill_create'),
        'Update': reverse('bill_update', args=['<str:pk>']),
        'Delete': reverse('bill_delete', args=['<str:pk>']),
        'Magic Link': reverse('send_magic_link_view'),
    }

    return Response(api_urls, status=status.HTTP_200_OK)

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
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def billUpdate(req, pk):
    bill = Bill.objects.get(id=pk)
    serializer = BillSerializer(instance=bill, data=req.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def billDelete(req, pk):
    bill = Bill.objects.get(id=pk)
    bill.delete()

    return Response('Item successfully deleted!', status=status.HTTP_204_NO_CONTENT) 


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
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def profileUpdate(req, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(instance=profile, data=req.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def profileDelete(req, pk):
    profile = Profile.objects.get(id=pk)
    profile.delete()

    return Response('Item successfully deleted!', status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def send_magic_link_view(request):
    if request.method == 'POST':
        email = request.data.get('email')
        magic_link = send_magic_link(email)

        profile_data = {'email': email}
        profile_serializer = ProfileSerializer(data=profile_data)

        if profile_serializer.is_valid():
            profile_serializer.save()

            return JsonResponse({'magic_link': magic_link, 'profile_id': profile_serializer.data['id']}, status=status.HTTP_201_CREATED)
        else:
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)