from django.db import models
from ckeditor.fields import RichTextField


class Language(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class TourCompanies(models.Model):
    comp_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='tour_companies/')
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.comp_name


class TourCategories(models.Model):
    title = models.CharField(max_length=50)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class TourGuides(models.Model):
    full_name = models.CharField(max_length=100)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name


class Tours(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    tour_companies = models.ForeignKey(TourCompanies, on_delete=models.CASCADE)
    tour_categories = models.ForeignKey(TourCategories, on_delete=models.CASCADE)
    tour_guides = models.ForeignKey(TourGuides, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tours/')
    price = models.FloatField(default=0)
    departure_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(auto_now_add=True)
    is_new = models.BooleanField(default=False)
    max_people = models.IntegerField(default=0)

    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title