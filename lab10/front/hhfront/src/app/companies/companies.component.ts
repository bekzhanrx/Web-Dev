import {Component, OnInit} from '@angular/core';
import {Company} from "../models";
import {CompanyServiceService} from "../company-service.service";
import {RouterModule} from "@angular/router";
import {CommonModule} from "@angular/common";

@Component({
  selector: 'app-companies',
  standalone: true,
  imports: [RouterModule, CommonModule],
  templateUrl: './companies.component.html',
  styleUrl: './companies.component.css'
})
export class CompaniesComponent implements OnInit{
  companies!: Company[];
  loaded: boolean = false

  constructor(private companiesService: CompanyServiceService) {
  }

  ngOnInit() {
    this.loaded = false;
    this.companiesService.getCompanies().subscribe((companies) =>
    {
      this.companies = companies;
      this.loaded = true
    }
    )
  }

}
