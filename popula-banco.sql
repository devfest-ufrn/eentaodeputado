use eentaodeputado;

load data local infile '/data/deputados.csv' into table deputado fields terminated by ','
  enclosed by '"'
  lines terminated by '\n'
    (ideCadastro, codOrcamento, condicao,	
    	matricula, idParlamentar, nome, nomeParlamentar,urlFoto, sexo, uf, partido, gabinete, anexo, fone, email, comissoes);


