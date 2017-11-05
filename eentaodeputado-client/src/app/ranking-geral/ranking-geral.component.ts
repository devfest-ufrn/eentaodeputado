import { Component, OnInit } from '@angular/core';
import { DeputadoService } from '../deputado.service';
import { Deputado } from '../models/deputado';

@Component({
  selector: 'app-ranking-geral',
  templateUrl: './ranking-geral.component.html',
  styleUrls: ['./ranking-geral.component.css']
})
export class RankingGeralComponent implements OnInit {

	deputados: Array<Deputado> = [];

	constructor(private deputadoService: DeputadoService) { }

  	ngOnInit()
  	{
  		this.loadDeputados();
  	}

  	loadDeputados()
  	{
  		this.deputadoService.loadDeputados();
  		this.deputados = this.deputadoService.getDeputados();
  	}

}
