from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    address = models.TextField()

    class Meta:
        verbose_name_plural = "Companies"
        verbose_name = "Company"


class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE,
        related_name="vacancies"
    )

    class Meta:
        verbose_name_plural = "Vacancies"
        verbose_name = "Vacancy"

