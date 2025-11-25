from rest_framework import serializers
from apps.tour.models import Tours, TourGuides, TourCategories,TourCompanies, Language


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

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'