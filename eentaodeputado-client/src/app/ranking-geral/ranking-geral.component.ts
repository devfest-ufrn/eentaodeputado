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
  linkPreviousPage: string;

	constructor(private deputadoService: DeputadoService) { }

	ngOnInit()
	{
		this.init();
    this.isDeputado = false;
	}

	init() : void 
	{
		this.deputadoService
				.loadAllDeputados()
				.subscribe(data => {

					this.deputados = data['results'];
          
          this.linkPreviousPage = data['previous'];
          this.linkNextPage = data['next'];

				});
	}

  detailsDeputado(id: number)
  {
    this.isDeputado = true;

    this.deputadoService
        .loadDeputadoByID(id)
        .subscribe(data => {
    
          this.deputado = data;
          this.showModalDetail();
    
        });
  }
  
  togglePage(tipo: string)
  {
    var url = this.linkNextPage;

    if (tipo == 'prev') {
      url = this.linkPreviousPage; 
    }
    
    this.deputadoService
          .loadDeputadosByURI(url)
          .subscribe(data => {

            this.deputados = data['results'];
            
            this.linkPreviousPage = data['previous'];
            this.linkNextPage = data['next'];
          });
  }

  showModalDetail()
  {
    $('deputadoDetalhes').modal('show');
  }

}
