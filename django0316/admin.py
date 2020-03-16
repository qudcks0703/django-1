from django.contrib import admin

# Register your models here.
from .models import University, Student
from .forms import UniversityForm

@admin.register(University)
class CountryAmin(admin.ModelAdmin):
    form = UniversityForm
#폼까지 설정한거임.
@admin.register(Student)
class PostAmin(admin.ModelAdmin):
    pass