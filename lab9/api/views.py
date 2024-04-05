from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer


def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_company(request, pk=None):
    if request.method == 'GET':
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data, safe=False)


def get_vacancy_by_company(request, pk=None):
    if request.method == 'GET':
        try:
            company = get_object_or_404(Company, pk=pk)
            vacancies = Vacancy.objects.filter(company=company)
            serializer = VacancySerializer(vacancies, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            })


def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_vacancy(request,pk=None):
    if request.method == 'GET':
        vacancy = get_object_or_404(Vacancy, pk=pk)
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data, safe=False)


def get_top10(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all().order_by('-salary')[:10]
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)