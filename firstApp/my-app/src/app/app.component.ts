import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {MynewcomponentComponent} from "./mynewcomponent/mynewcomponent.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, MynewcomponentComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Web Developer Blog';
}
