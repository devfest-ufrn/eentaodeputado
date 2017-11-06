import { Injectable } from '@angular/core';
import { Deputado } from './models/deputado';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';


@Injectable()
export class DeputadoService {

	baseUrl = "http://127.0.0.1:8000/";
	deputados: Deputado[];

	constructor(private http: HttpClient){ }

	loadDeputados()
	{
		var endpoint = 'api/deputados/?format=json';
		
		return this.http.get(this.baseUrl+endpoint)
				.map(res => res as Deputado[]);
				
	}

	getDeputados()
	{
		return this.deputados;
	}

}
