from django.urls import path, re_path
from .views.past_views import get_vacancy_by_company,get_top10
from api.views import CompanyDetailAPIView, CompanyListAPIView
from api.views import vacancy_detail, vacancy_list

urlpatterns = [
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view()),
    path('companies/<int:pk>/vacancies', get_vacancy_by_company),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:pk>', vacancy_detail),
    path('vacancies/top_ten', get_top10)
]