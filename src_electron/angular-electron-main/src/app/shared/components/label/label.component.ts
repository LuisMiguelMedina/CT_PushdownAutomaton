import { Component, Input } from '@angular/core'

@Component({
  selector: 'app-label',
  templateUrl: 'label.component.html',
  styleUrls: ['label.component.css'],
})
export class Label {
  @Input()
  text: string = 'Text'
  constructor() {}
}
