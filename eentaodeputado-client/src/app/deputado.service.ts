import { Injectable } from '@angular/core';
import { Deputado } from './models/deputado';

@Injectable()
export class DeputadoService {

	deputados: Array<Deputado> = [];

	constructor(){ }

	loadDeputados(): void
	{
		var tam = 10;
		for (var i = 0; i < tam; i++) {
			this.deputados.push(new Deputado('Teste'+i, 'teste'));
		}
	}

	getDeputados() : Array<Deputado>
	{
		return this.deputados;
	}

}
