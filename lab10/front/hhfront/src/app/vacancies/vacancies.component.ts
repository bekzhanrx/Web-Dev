import {Component, OnInit} from '@angular/core';
import {Vacancy} from "../models";
import {VacancyServiceService} from "../vacancy-service.service";
import {ActivatedRoute, RouterModule} from "@angular/router";
import {CommonModule, NgForOf, NgIf} from "@angular/common";

@Component({
  selector: 'app-vacancies',
  standalone: true,
  imports: [
    RouterModule,
    CommonModule
  ],
  templateUrl: './vacancies.component.html',
  styleUrl: './vacancies.component.css'
})
export class VacanciesComponent implements OnInit{
  vacancies!: Vacancy[]
  loaded: boolean = false

  constructor(private service: VacancyServiceService,
              private route: ActivatedRoute) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe((params)=> {
      if (params.get('id')){
        const companyId = Number(params.get('id'))
        this.loaded = false;
        this.service.getVacancies(companyId).subscribe((vacancies)=>{
          this.vacancies = vacancies;
          this.loaded = true;
        });
      }
    })

  }

}
