from apps.sadaqa.models import (
    Language, HelpCategory, HelpRequest,
    MaterialsStatus, Post, Company, Note,
)
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from apps.sadaqa.serializer import (
    LanguageSerializer, HelpRequestSerializer,
    HelpCategorySerializer, PostSerializer,
    CompanySerializer,  MaterialsStatusSerializer,
    NoteSerializer
)


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


class MaterialsStatusViewSet(viewsets.ModelViewSet):
    queryset = MaterialsStatus.objects.all()
    serializer_class = MaterialsStatusSerializer
    permission_classes = [permissions.AllowAny]


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MaterialsStatusSerializer(queryset, many=True)
        return Response({
            "status": True,
            "count": len(serializer.data),
            "data": serializer.data
        })


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer(queryset, many=True)
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response({
            "status": True,
            "count": len(serializer.data),
            "data": serializer.data
        })

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CompanySerializer(queryset, many=True)
        return Response({
            "status": True,
            "count": len(serializer.data),
            "data": serializer.data
        })


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = NoteSerializer(queryset, many=True)
        return Response({
            "status": True,
            "count": len(serializer.data),
            "data": serializer.data
        })






