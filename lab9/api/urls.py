from django.urls import path, re_path
from .views import company_list, get_company, get_vacancy_by_company, vacancy_list, get_vacancy, get_top10

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:pk>/', get_company),
    path('companies/<int:pk>/vacancies', get_vacancy_by_company),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:pk>', get_vacancy),
    path('vacancies/top_ten', get_top10)
]