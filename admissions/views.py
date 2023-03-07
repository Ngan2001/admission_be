from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import Admissions
from .serializers import AdmissionSerializer

class AdmissionViewSet(viewsets.ModelViewSet):

    queryset = Admissions.objects.filter(active=True)
    serializer_class = AdmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
