from rest_framework import viewsets, permissions
from rest_framework.response import Response
from apps.sadaqa.models import Language, HelpCategory, HelpRequest
from apps.sadaqa.serializer import LanguageSerializer, HelpRequestSerializer, HelpCategorySerializer


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

class HelpCategoryViewSet(viewsets.ModelViewSet):
    queryset = HelpCategory.objects.all()
    serializer_class = HelpCategorySerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = HelpCategorySerializer(queryset, many=True)
        return Response({
            "status": True,
            "count": len(serializer.data),
            "data": serializer.data
        })


class HelpRequestViewSet(viewsets.ModelViewSet):
    queryset = HelpRequest.objects.all()
    serializer_class = HelpRequestSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = HelpRequestSerializer(queryset, many=True)
        return Response({
            "status": True,
            "count": len(serializer.data),
            "data": serializer.data
        })




