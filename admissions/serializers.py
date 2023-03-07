from rest_framework.serializers import ModelSerializer
from .models import Admissions

class AdmissionSerializer(ModelSerializer):
    class Meta:
        model = Admissions
        fields =[ 'title' , 'content']
