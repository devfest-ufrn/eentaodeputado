import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { SobreComponent } from './sobre/sobre.component';
import { RankingGeralComponent } from './ranking-geral/ranking-geral.component';


import { DeputadoService } from './deputado.service';
import { ListagemGeralComponent } from './listagem-geral/listagem-geral.component';
import { FilterPipe } from './filter.pipe';



const appRoutes: Routes = [
	{ 
		path: '',
		component: RankingGeralComponent
	},
	{
		path: 'sobre',
		component: SobreComponent
	}, 
  {
    path: 'listagem-geral',
    component: ListagemGeralComponent
  }
]

@NgModule({
  declarations: [
    AppComponent,
    SobreComponent,
    RankingGeralComponent,
    ListagemGeralComponent,
    FilterPipe
  ],
  imports: [
    BrowserModule,
    FormsModule,    
    HttpClientModule,
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // <-- debugging purposes only
    )
  ],
  providers: [DeputadoService],
  bootstrap: [AppComponent]
})
export class AppModule { }
