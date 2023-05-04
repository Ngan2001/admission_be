from django.contrib.auth.models import User
from django.http import HttpResponse
# from requests import Response
from rest_framework.response import Response
from rest_framework import viewsets, permissions, parsers, status
from rest_framework.decorators import action

from .models import *
from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from .models import Admissions, AdmissionType
from .serializers import AdmissionSerializer, AdmissionTypeSerializer, UserSerializer
import smtplib


class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admissions.objects.all()
    serializer_class = AdmissionSerializer

    @action(methods=['get'], detail=False, url_path='get-all-no-paging')
    def get_all_no_paging(self, request):
        admissions = Admissions.objects.all()

        serializer = AdmissionSerializer(admissions, many=True)

        return Response(serializer.data,
                        status=status.HTTP_200_OK)


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

    @action(methods=['get', 'post'], detail=False, url_path='send-mail')
    def send_mail(self, request):
        sender = 'from@example.com'
        receivers = ['to@example.com']
        message = """
        From: From Person <from@example.com>
        To: To Person <to@example.com>
        Subject: SMTP email example


        This is a test message.
        """

        try:
            smtpObj = smtplib.SMTP('localhost')
            smtpObj.sendmail(sender, receivers, message)
            print("Successfully sent email")
        except smtplib.SMTPException:
            pass

        return Response()

class AdmissionTypeViewSet(viewsets.ModelViewSet):
    queryset = AdmissionType.objects.all()
    serializer_class = AdmissionTypeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    paginate_class = None

    def paginate_queryset(self, queryset):
            return None

    def get_queryset(self):
        admissionId = self.request.query_params.get('admissionId')
        if  admissionId is None:
            return  Comment.objects.all()
        else:
            return  Comment.objects.filter(admissions_id=admissionId)
        # return queryset


    # @action(methods=['get'], detail=True,
    #         name='Get comments by admission id',
    #         url_path='get-comments-by-admission-id',
    #         url_name='get-comments-by-admission-id')
    # def hide_lesson(self, request, pk=None):
    #     comment = Comment.objects.get(pk=pk)
    #     serializer = CommentSerializer(comment)
    #     return Response(serializer.data,
    #                     status=status.HTTP_200_OK)


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

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

