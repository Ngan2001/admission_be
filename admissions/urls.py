from django.urls import path, include
from rest_framework import routers

from admissions import views

router = routers.DefaultRouter()
router.register('admission', views.AdmissionViewSet),
router.register('user-role', views.UserRoleViewSet),
router.register('user', views.UserViewSet),
router.register('admission-type', views.AdmissionTypeViewSet),
router.register('comment', views.CommentViewSet),
router.register('banner', views.BannerViewSet),
router.register('department', views.DepartmentViewSet),
router.register('livestreamscomment', views.LivestreamsCommentViewSet),
router.register('livestreamsnotification', views.LivestreamsNotificationViewSet),
router.register('frequentlyquestions', views.FrequentlyQuestionsViewSet),
router.register('admissionsquestiontimeRange', views.AdmissionsQuestionTimeRangeViewSet),
router.register('admissionsquestion', views.AdmissionsQuestionViewSet),

urlpatterns = [
    path('', include(router.urls))
]