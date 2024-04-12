from django.contrib import admin


from api.models import Company, Vacancy


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)


@admin.register(Vacancy)
class Vacancy(admin.ModelAdmin):
    list_display = ('name', 'salary')
    search_fields = ('salary',)



