import { BrowserModule } from '@angular/platform-browser';
import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { CoreModule } from './core/core.module';
import { SharedModule } from './shared/shared.module';

import { AppRoutingModule } from './app-routing.module';

// NG Translate
import { TranslateModule, TranslateLoader } from '@ngx-translate/core';
import { TranslateHttpLoader } from '@ngx-translate/http-loader';

import { HomeModule } from './pages/home/home.module';
import { DetailModule } from './pages/detail/detail.module';

import { AppComponent } from './app.component';
import { RouterModule } from '@angular/router';
import { ComponentsModule } from './shared/components/componentes.module';

// AoT requires an exported function for factories
const httpLoaderFactory = (http: HttpClient): TranslateHttpLoader =>  new TranslateHttpLoader(http, './assets/i18n/', '.json');

const routes = [
  {
    path: '',
    loadChildren: () =>
      import('./pages/home/home.module').then((m) => m.HomeModule),
  },
  {
    path: '**',
    loadChildren: () =>
      import('./shared/components/page-not-found/page-not-found.component').then(
        (m) => m.PageNotFoundComponent
      ),
  },
];

@NgModule({
  declarations: [AppComponent],
  providers: [],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(routes),
    ComponentsModule,
    CoreModule,
    SharedModule,
    HomeModule,
    DetailModule,
    AppRoutingModule,
    TranslateModule.forRoot({
      loader: {
        provide: TranslateLoader,
        useFactory: httpLoaderFactory,
        deps: [HttpClient]
      }
    })
  ],
})
export class AppModule {}

