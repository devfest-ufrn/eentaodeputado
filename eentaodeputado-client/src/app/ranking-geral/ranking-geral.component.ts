import { Component, OnInit } from '@angular/core';
import { DeputadoService } from '../deputado.service';
import { Deputado } from '../models/deputado';
import { Observable } from 'rxjs/Observable';

declare var jquery:any;
declare var $ :any;


enum RankingBy {
  state = 1,
  general = 0
};

@Component({
  selector: 'app-ranking-geral',
  templateUrl: './ranking-geral.component.html',
  styleUrls: ['./ranking-geral.component.css']
})
export class RankingGeralComponent implements OnInit {

  estados: string[];
  deputados: Deputado[];
  deputado: Deputado;

  estadoSelected: string;
  isDeputado: boolean;
  
  linkNextPage: string;
  linkPreviousPage: string;

  rankingBy: RankingBy;

	constructor(private deputadoService: DeputadoService) { }

	ngOnInit()
	{
		this.init();
    this.isDeputado = false;
    this.rankingBy = 0;
    this.estadoSelected = "0";
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

    this.estados = this.deputadoService
                            .loadEstados();
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
  
  deputadosByEstado()
  {

    this.deputadoService
          .loaddeputadosByUF(this.estadoSelected)
          .subscribe(data => {
            this.deputados = data['results'];
            
            this.linkPreviousPage = data['previous'];
            this.linkNextPage = data['next'];

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

  isDisable(tipo: string)
  {
    if (tipo == 'prev') {
      if (this.linkPreviousPage == null) {
        return 'disabled';
      }
    }

    if (tipo == 'next') {
      if (this.linkNextPage == null) {
        return 'disabled';
      }
    }

  }
  showModalDetail()
  {
    $('deputadoDetalhes').modal('show');
  }

}
