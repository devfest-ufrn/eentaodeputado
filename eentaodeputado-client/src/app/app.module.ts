import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';


import { AppComponent } from './app.component';
import { SobreComponent } from './sobre/sobre.component';
import { RankingGeralComponent } from './ranking-geral/ranking-geral.component';


const appRoutes: Routes = [
	{ 
		path: '',
		component: RankingGeralComponent
	},
	{
		path: 'sobre',
		component: SobreComponent
	}
]

@NgModule({
  declarations: [
    AppComponent,
    SobreComponent,
    RankingGeralComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,

    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // <-- debugging purposes only
    )
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
