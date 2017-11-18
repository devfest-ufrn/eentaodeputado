import { Component, OnInit } from '@angular/core';
import { DeputadoService } from '../deputado.service';
import { Deputado } from '../models/deputado';
import { Observable } from 'rxjs/Observable';

declare var jquery:any;
declare var $ :any;

@Component({
  selector: 'app-ranking-geral',
  templateUrl: './ranking-geral.component.html',
  styleUrls: ['./ranking-geral.component.css']
})
export class RankingGeralComponent implements OnInit {

	deputados: Deputado[];
  deputado: Deputado;
  isDeputado: boolean;
  linkNextPage: string;

	constructor(private deputadoService: DeputadoService) { }

	ngOnInit()
	{
		this.loadDeputados();
    this.isDeputado = false;
	}

	loadDeputados() : void 
	{
		this.deputadoService
				.loadAllDeputados()
				.subscribe(data => {
          this.linkNextPage = data['next'];
					this.deputados = data['results'];
				});
	}

  detailsDeputado(id: number)
  {
    this.isDeputado = true;

    this.deputadoService
        .loadDeputadoByID(id)
        .subscribe(data => {
    
          this.deputado = data;
          $('deputadoDetalhes').modal('show');
    
        });



  }

  nextPage(): void
  {
    
  }

}
