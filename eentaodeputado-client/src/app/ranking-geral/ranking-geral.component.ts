import { Component, OnInit } from '@angular/core';
import { DeputadoService } from '../deputado.service';
import { Deputado } from '../models/deputado';
import { Observable } from 'rxjs/Observable';


@Component({
  selector: 'app-ranking-geral',
  templateUrl: './ranking-geral.component.html',
  styleUrls: ['./ranking-geral.component.css']
})
export class RankingGeralComponent implements OnInit {

	deputados: Deputado[];
	constructor(private deputadoService: DeputadoService) { }

  	ngOnInit()
  	{
  		this.loadDeputados();
  	}

  	loadDeputados()
  	{
  		this.deputadoService.loadDeputados().subscribe(data => this.deputados = data);
  	}

}
