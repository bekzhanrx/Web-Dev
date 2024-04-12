import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Company, Vacancy
from api.serializers import CompanySerializer2, VacancySerializer


@api_view(["GET", "POST"])
def company_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        serializer = CompanySerializer2(companies, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = json.loads(request.body)
        serializer = CompanySerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])
def company_detail(request, pk=None):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return Response({"error": str(e)})
    if request.method == "GET":
        serializer = CompanySerializer2(company)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CompanySerializer2(
            instance=company,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    elif request.method =="DELETE":
        company.delete()
        return Response({"deleted": True})


@api_view(["GET","POST"])
def vacancy_list(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = json.loads(request.body)
        serializer = VacancySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


@api_view(["GET","PUT","DELETE"])
def vacancy_detail(request, pk=None):
    try:
        vacancy = Vacancy.objects.get(id=pk)
    except Vacancy.DoesNotExist as e:
        return Response({"error": str(e) })
    if request.method == "GET":
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = VacancySerializer(
            instance=vacancy,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    elif request.method == "DELETE":
        vacancy.delete()
        return Response({"deleted": True})


