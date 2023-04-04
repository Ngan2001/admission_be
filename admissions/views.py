from django.contrib.auth.models import User
from django.http import HttpResponse
from requests import Response
from rest_framework import viewsets, permissions, parsers
from rest_framework.decorators import action

from .models import *
from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from .models import Admissions, AdmissionType
from .serializers import AdmissionSerializer, AdmissionTypeSerializer, UserSerializer


class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admissions.objects.all()
    serializer_class = AdmissionSerializer




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser, ]

    def get_permissions(self):
        if self.action in ['current_user']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get', 'put'], detail=False, url_path='current-user')
    def current_user(self, request):
        u = request.user
        if request.method.__eq__('PUT'):
            for k, v in request.data.items():
                setattr(u, k, v)
            u.save()

        return Response(UserSerializer(u, context={'request': request}).data)

class AdmissionTypeViewSet(viewsets.ModelViewSet):
    queryset = AdmissionType.objects.all()
    serializer_class = AdmissionTypeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class LivestreamsNotificationViewSet(viewsets.ModelViewSet):
    queryset = LivestreamsNotification.objects.all()
    serializer_class = LivestreamsNotificationSerializer


class LivestreamsCommentViewSet(viewsets.ModelViewSet):
    queryset = LivestreamsComment.objects.all()
    serializer_class = LivestreamsCommentSerializer


class FrequentlyQuestionsViewSet(viewsets.ModelViewSet):
    queryset = FrequentlyQuestions.objects.all()
    serializer_class = FrequentlyQuestionsSerializer


class AdmissionsQuestionTimeRangeViewSet(viewsets.ModelViewSet):
    queryset = AdmissionsQuestionTimeRange.objects.all()
    serializer_class = AdmissionsQuestionTimeRangeSerializer

class AdmissionsQuestionViewSet(viewsets.ModelViewSet):
    queryset = AdmissionsQuestion.objects.all()
    serializer_class = AdmissionsQuestionSerializer

