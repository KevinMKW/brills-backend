from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Profile, Bill
from .serializers import ProfileSerializer, BillSerializer

class ProfileAPIView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class Profile(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class BillAPIView(ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class Bill(RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer