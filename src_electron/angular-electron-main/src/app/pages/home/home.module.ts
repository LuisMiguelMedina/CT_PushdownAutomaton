import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { RouterModule } from '@angular/router'
import { CommonModule } from '@angular/common'

import { SharedModule } from '../../shared/shared.module'
import { HomeComponent } from './home.component'

const routes = [
  {
    path: '',
    component: HomeComponent,
  },
]

@NgModule({
  declarations: [HomeComponent],
  imports: [CommonModule, SharedModule, RouterModule.forChild(routes)],
  exports: [HomeComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class HomeModule {}

// ../../assets/images/AutomataDePila.jpg
