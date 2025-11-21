from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Product
from .serializer import LanguageSerializer, HelpRequestSerializer, HelpCategorySerializer, TourCompanySerializer, ToursSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.Allow]


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = LanguageSerializer(queryset, many=True)
        return Response({
            "status": True,
            "count": len(serializer.data),
            "data": serializer.data
        })




