import { Component, Input } from '@angular/core'

@Component({
  selector: 'user-details',
  templateUrl: 'user-details.component.html',
  styleUrls: ['user-details.component.css'],
})
export class UserDetails {
  @Input()
  image_src: string =
    'https://play.teleporthq.io/static/svg/placeholders/no-image.svg'
  @Input()
  name: string = 'Laura Hanks'
  @Input()
  time: string = '3 days'
  @Input()
  image_alt: string = 'image'
  raw54oz: string = ' '
  constructor() {}
}
