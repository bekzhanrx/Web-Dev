import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Vacancy} from "./models";

@Injectable({
  providedIn: 'root'
})
export class VacancyServiceService {

  constructor(private client:HttpClient) { }

  getVacancies(id:number):Observable<Vacancy[]>{
    return this.client.get<Vacancy[]>(`http://127.0.0.1:8000/api/companies/${id}/vacancies`)
  }
  getVacancy(id: number):Observable<Vacancy>{
    return this.client.get<Vacancy>(`http://127.0.0.1:8000/api/vacancies/${id}`)
  }
}
