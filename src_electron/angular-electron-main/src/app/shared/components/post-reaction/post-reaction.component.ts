import { Component, Input } from '@angular/core'

@Component({
  selector: 'post-reaction',
  templateUrl: 'post-reaction.component.html',
  styleUrls: ['post-reaction.component.css'],
})
export class PostReaction {
  @Input()
  image_src: string =
    'https://play.teleporthq.io/static/svg/placeholders/no-image.svg'
  @Input()
  name: string = 'John Snow'
  @Input()
  image_alt: string = 'image'
  @Input()
  likes: string = '10'
  @Input()
  text: string =
    'You have the opportunity to play this game of life you need to appreciate every moment.'
  @Input()
  shares: string = '2'
  constructor() {}
}
