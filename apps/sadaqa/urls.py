from rest_framework.routers import DefaultRouter
from apps.sadaqa.views import LanguageViewSet, HelpCategoryViewSet, HelpRequestViewSet

router = DefaultRouter()
router.register('language', LanguageViewSet)
router.register('help_category', HelpCategoryViewSet)
router.register('help_request', HelpRequestViewSet)

urlpatterns = router.urls