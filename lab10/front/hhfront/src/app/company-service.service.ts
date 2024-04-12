import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Company} from "./models";
import {Observable} from "rxjs";
@Injectable({
  providedIn: 'root'
})
export class CompanyServiceService {
  constructor(private client: HttpClient) { }
  getCompanies(): Observable<Company[]>{
    return this.client.get<Company[]>('http://127.0.0.1:8000/api/companies/');
  }
  getCompany(id: number): Observable<Company>{
    return this.client.get<Company>(`http://127.0.0.1:8000/api/companies/${id}/`)
  }
}
