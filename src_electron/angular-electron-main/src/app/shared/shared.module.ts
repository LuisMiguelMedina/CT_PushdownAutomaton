import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { TranslateModule } from '@ngx-translate/core';

import { PageNotFoundComponent } from './components/page-not-found/page-not-found.component';
import { WebviewDirective } from './directives/';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [PageNotFoundComponent, WebviewDirective],
  imports: [CommonModule, TranslateModule, FormsModule],
  exports: [TranslateModule, WebviewDirective, FormsModule, PageNotFoundComponent]
})
export class SharedModule {}
export { PageNotFoundComponent };

