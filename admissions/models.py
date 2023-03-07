from django.db import models
from django.contrib.auth.models import User


class ModelBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-id'] # sắp giảm theo id

class User_role(models.Model):
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return self.role_name


class User(User):

    birthday_date = models.DateTimeField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    avata = models.CharField(max_length=10)
    active = models.BooleanField(default=True)



class Admission_type(models.Model):
    type_name = models.CharField(max_length=100)
    decription = models.TextField()

    def __str__(self):
        return self.type_name


class Admissions(models.Model):

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    type_id = models.ForeignKey(Admission_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):

    content = models.TextField()
    feedback_comment_id = models.IntegerField()
    origin_comment_id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    admissions_id = models.ForeignKey(Admissions,on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Banner(models.Model):
    image_url = models.ImageField()
    description = models.TextField()
    link_url = models.TextField()
    position = models.TextField()

    def __str__(self):
        return self.image_url

class department(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50)
    introduction = models.CharField(max_length=50)
    content = models.TextField()
    website = models.TextField()
    video_url = models.TextField()

    def __str__(self):
        return self.image

class livestreams_notification(models.Model):
    content = models.TextField()
    start_date = models.DateTimeField()
    time = models.IntegerField()

    def __str__(self):
        return self.content

class livestreams_comment(models.Model):
    content = models.TextField()
    livestreams_id = models.IntegerField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class frequently_questions(models.Model):
    question_content = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question_content

class admissions_question_time_range(models.Model):
    is_fullday = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.is_fullday

class admissions_question(models.Model):
    question = models.TextField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_answer = models.TextField()
    date_answer = models.DateTimeField()

    def __str__(self):
        return self.question


