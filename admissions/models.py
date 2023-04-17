from django.db import models
from django.contrib.auth.models import User, AbstractUser


class ModelBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-id'] # sắp giảm theo id




class User(AbstractUser):
    birthday_date = models.DateTimeField(null=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to="users/%Y/%m/", null=True)

class AdmissionType(models.Model):
    type_name = models.CharField(max_length=100)
    decription = models.TextField()

    def __str__(self):
        return self.type_name


class Admissions(ModelBase):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail_image = models.ImageField(upload_to="admissions/%Y/%m/", null=True)
    admission_type = models.ForeignKey(AdmissionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(ModelBase):

    content = models.TextField()
    feedback_comment_id = models.IntegerField(null=True)
    origin_comment_id = models.IntegerField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    admissions_id = models.ForeignKey(Admissions,on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_date']  # sắp tăng theo ngày tạo

    def __str__(self):
        return self.content

class Banner(ModelBase):
    image_url = models.ImageField(upload_to="banner/%Y/%m/")


class Department(ModelBase):
    image = models.ImageField(upload_to="department/%Y/%m/")
    name = models.CharField(max_length=50)
    content = models.TextField()
    website = models.TextField()
    video_url = models.TextField(null=True)

    def __str__(self):
        return self.image

class LivestreamsNotification(ModelBase):
    title = models.TextField(null = True)
    content = models.TextField()
    start_date = models.DateTimeField()
    time = models.IntegerField()

    def __str__(self):
        return self.content

class LivestreamsComment(ModelBase):
    content = models.TextField()
    livestreams_id = models.IntegerField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class FrequentlyQuestions(ModelBase):
    question_content = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question_content

class AdmissionsQuestionTimeRange(ModelBase):
    is_fullday = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.is_fullday

class AdmissionsQuestion(ModelBase):
    question = models.TextField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_answer = models.TextField()
    date_answer = models.DateTimeField()

    def __str__(self):
        return self.question


