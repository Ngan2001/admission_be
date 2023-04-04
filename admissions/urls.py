from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from admissionapp import settings
from . import views
from rest_framework import routers
from django.contrib.staticfiles.urls import static

router = routers.DefaultRouter()
router.register('admission', views.AdmissionViewSet),
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
# router.register('user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)