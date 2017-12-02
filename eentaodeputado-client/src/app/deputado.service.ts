import { Injectable } from '@angular/core';
import { Deputado } from './models/deputado';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';


@Injectable()
export class DeputadoService {

	estados: string[];
	baseUrl = "http://127.0.0.1:8000/api/";

	constructor(private http: HttpClient){ 
		this.estados = [
						'AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG',
						'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN',
						'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'
					];

	}

	loadAllDeputados()
	{
		var endpoint = 'deputados/?format=json';
		
		return this.http.get(this.baseUrl+endpoint);				
	}

	loadDeputadoByID(id: number)
	{
		var endpoint = 'deputados/'+id;
		
		return this.http.get(this.baseUrl+endpoint)
					.map(res => res as Deputado);
	}

	loadDeputadosByURI(url: string)
	{
		return this.http.get(url);
	}

	loaddeputadosByUF(uf: string)
	{
		var endpoint = 'deputados/uf/'+uf+'/?format=json';

		return this.http.get(this.baseUrl+endpoint);
	}

	loadEstados(): string[]
	{
		return this.estados;
	}
}
