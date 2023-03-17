from rest_framework.serializers import ModelSerializer
from .models import *


class AdmissionSerializer(ModelSerializer):
    class Meta:
        model = Admissions
        fields = ['title', 'content']


class UserRoleSerializer(ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['role_name', 'created_date', 'updated_date']




class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(user.password)
        user.save()
        return user

class AdmissionTypeSerializer(ModelSerializer):
    class Meta:
        model = AdmissionType
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class LivestreamsNotificationSerializer(ModelSerializer):
    class Meta:
        model = LivestreamsNotification
        fields = '__all__'


class LivestreamsCommentSerializer(ModelSerializer):
    class Meta:
        model = LivestreamsComment
        fields = '__all__'


class FrequentlyQuestionsSerializer(ModelSerializer):
    class Meta:
        model = FrequentlyQuestions
        fields = '__all__'


class AdmissionsQuestionTimeRangeSerializer(ModelSerializer):
    class Meta:
        model = AdmissionsQuestionTimeRange
        fields = '__all__'


class AdmissionsQuestionSerializer(ModelSerializer):
    class Meta:
        model = AdmissionsQuestion
        fields = '__all__'
