import { Routes } from '@angular/router';
import {CompaniesComponent} from "./companies/companies.component";
import {VacanciesComponent} from "./vacancies/vacancies.component";

export const routes: Routes = [
  {path: 'companies', component: CompaniesComponent, title: 'Companies'},
  {path: '', redirectTo: 'companies', pathMatch: "full"},
  {path: 'companies/:id', component: VacanciesComponent, title: 'Vacancies by company'}
];
