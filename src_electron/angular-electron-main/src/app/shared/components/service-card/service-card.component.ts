import { Component, Input } from '@angular/core'

@Component({
  selector: 'service-card',
  templateUrl: 'service-card.component.html',
  styleUrls: ['service-card.component.css'],
})
export class ServiceCard {
  @Input()
  text: string =
    "Some quick example text to build on the card title and make up the bulk of the card's content."
  @Input()
  heading: string = 'Excelent services'
  constructor() {}
}
