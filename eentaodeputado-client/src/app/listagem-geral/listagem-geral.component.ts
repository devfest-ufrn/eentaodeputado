import { Component, OnInit } from '@angular/core';
import { DeputadoService } from '../deputado.service';
import { Deputado } from '../models/deputado';

@Component({
  selector: 'app-listagem-geral',
  templateUrl: './listagem-geral.component.html',
  styleUrls: ['./listagem-geral.component.css']
})
export class ListagemGeralComponent implements OnInit {

	deputados : Deputado[];
	detalheDeputado : Deputado;

  constructor(private deputadoService: DeputadoService) { }

  ngOnInit() {
  	this.init();
  }

  init() : void
  {
  	this.deputadoService
  				.loadAllDeputados()
  				.subscribe( data => {
  					this.deputados = data['results'];
  				});
  }

  detailsDeputado(id : number)
  {
  	this.deputadoService
  				.loadDeputadoByID(id)
  				.subscribe(data => {
  					this.detalheDeputado = data;
  				});
  }

}
