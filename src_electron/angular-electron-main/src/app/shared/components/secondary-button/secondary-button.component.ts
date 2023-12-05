import { Component, Input } from '@angular/core'

@Component({
  selector: 'secondary-button',
  templateUrl: 'secondary-button.component.html',
  styleUrls: ['secondary-button.component.css'],
})
export class SecondaryButton {
  @Input()
  button: string = 'Button'
  @Input()
  rootClassName: string = ''
  constructor() {}
}
