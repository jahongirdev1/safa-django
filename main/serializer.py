from rest_framework import serializers
from main.models import Language, Company, Post, MaterialsStatus, HelpRequest, HelpCategory, Note, TourCategories, TourCompanies, TourGuides, Tours


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class MaterialsStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialsStatus
        fields = '__all__'

class HelpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpRequest
        fields = '__all__'

class HelpCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpCategory
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class ToursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = '__all__'

class TourGuidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourGuides
        fields = '__all__'

class TourCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourCategories
        fields = '__all__'

class TourCompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourCompanies
        fields = '__all__'

