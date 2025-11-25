from apps.tour.serializer import (
    LanguageSerializer, ToursSerializer, TourGuidesSerializer,
    TourCategoriesSerializer, TourCompaniesSerializer
)
from apps.tour.models import (
    Language, Tours, TourGuides, TourCategories, TourCompanies
)
from rest_framework import viewsets, permissions
from rest_framework.response import Response


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = LanguageSerializer(queryset, many=True)
        return Response({
            "status": True,
            "count": len(serializer.data),
            "data": serializer.data
        })


class ToursViewSet(viewsets.ModelViewSet):
    queryset = Tours.objects.all()
    serializer_class = ToursSerializer
    permission_classes = [permissions.AllowAny]
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ToursSerializer(queryset, many=True)
        return Response({
            "status": True,
            "count": len(serializer.data),
            "data": serializer.data
        })

class TourGuidesViewSet(viewsets.ModelViewSet):
    queryset = TourGuides.objects.all()
    serializer_class = TourGuidesSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TourGuidesSerializer(queryset, many=True)
        return Response({
            "status": True,
            "count": len(serializer.data),
            "data": serializer.data
        })

class TourCategoriesViewSet(viewsets.ModelViewSet):
    queryset = TourCategories.objects.all()
    serializer_class = TourCategoriesSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TourCategoriesSerializer(queryset, many=True)
        return Response({
            "status": True,
            "count": len(serializer.data),
            "data": serializer.data
        })

class TourCompaniesViewSet(viewsets.ModelViewSet):
    queryset = TourCompanies.objects.all()
    serializer_class = TourCompaniesSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TourCompaniesSerializer(queryset, many=True)
        return Response({
            "status": True,
            "count": len(serializer.data),
            "data": serializer.data
        })


