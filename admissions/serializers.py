from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class AdmissionSerializer(ModelSerializer):
    thumbnail_image = Base64ImageField(max_length=None, use_url=True)
    admission_type_name = serializers.CharField(source='admission_type.type_name', read_only=True)
    class Meta:
        model = Admissions
        fields = ['id', 'title', 'content', 'thumbnail_image', 'admission_type', 'admission_type_name']


class AdmissionTypeSerializer(ModelSerializer):
    class Meta:
        model = AdmissionType
        fields =[ 'type_name' , 'decription']



class UserSerializer(ModelSerializer):
    avatar = Base64ImageField(max_length=None, use_url=True)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'avatar', 'address', 'birthday_date', 'phone', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(user.password)
        user.save()
        return user

    def update(self, validated_data):
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
    username = serializers.CharField(source='user_id.username', read_only=True)
    avatar = serializers.ImageField(source='user_id.avatar', read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_date', 'admissions_id', 'origin_comment_id', 'user_id', 'username', 'avatar')


class BannerSerializer(ModelSerializer):
    image_url = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Banner
        fields = '__all__'

class SchoolSerializer(ModelSerializer):
    logo = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = School
        fields = '__all__'

class DepartmentSerializer(ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Department
        fields = '__all__'


class LivestreamsNotificationSerializer(ModelSerializer):
    class Meta:
        model = LivestreamsNotification
        fields = '__all__'


class LivestreamsCommentSerializer(ModelSerializer):
    username = serializers.CharField(source='user_id.username', read_only=True)
    class Meta:
        model = LivestreamsComment
        fields = ('id', 'content', 'created_date', 'livestreams_id', 'user_id', 'username')

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

