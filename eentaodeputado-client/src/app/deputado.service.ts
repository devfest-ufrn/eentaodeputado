import { Injectable } from '@angular/core';
import { Deputado } from './models/deputado';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';


@Injectable()
export class DeputadoService {

	baseUrl = "http://127.0.0.1:8000/api/";

	constructor(private http: HttpClient){ }

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
}
