from rest_framework.routers import DefaultRouter
from apps.tour.models import (
    Language, Tours, TourGuides,
    TourCompanies, TourCategories,
)
from apps.tour.views import (
    LanguageViewSet, ToursViewSet, TourGuidesViewSet,
    TourCompaniesViewSet, TourCategoriesViewSet,
)

router = DefaultRouter()
router.register('languages', LanguageViewSet)
router.register('tours', ToursViewSet)
router.register('guides', TourGuidesViewSet)
router.register('companies', TourCompaniesViewSet)
router.register('categories', TourCategoriesViewSet)

urlpatterns = router.urls
