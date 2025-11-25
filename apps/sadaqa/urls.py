from rest_framework.routers import DefaultRouter
from apps.sadaqa.models import (
    Language, HelpCategory, HelpRequest,
    MaterialsStatus, Post, Company, Note,
)
from apps.sadaqa.views import (
    LanguageViewSet, HelpCategoryViewSet, HelpRequestViewSet,
    MaterialsStatusViewSet, PostViewSet, CompanyViewSet, NoteViewSet,
)

router = DefaultRouter()
router.register('language', LanguageViewSet)
router.register('help_category', HelpCategoryViewSet)
router.register('help_request', HelpRequestViewSet)
router.register('materials_status', MaterialsStatusViewSet)
router.register('post', PostViewSet)
router.register('company', CompanyViewSet)
router.register('note', NoteViewSet)

urlpatterns = router.urls