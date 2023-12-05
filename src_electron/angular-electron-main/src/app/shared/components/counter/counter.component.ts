import { Component, Input } from '@angular/core'

@Component({
  selector: 'app-counter',
  templateUrl: 'counter.component.html',
  styleUrls: ['counter.component.css'],
})
export class Counter {
  @Input()
  type: string = 'Friends'
  @Input()
  number: string = '22'
  constructor() {}
}
