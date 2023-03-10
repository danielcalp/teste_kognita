![KOGNITA_RGB_LOGO_COMPLETO_ROXO_ROSA](https://user-images.githubusercontent.com/81701366/215144953-33d142f6-a2ec-4105-93cf-5d1a3f80ec57.png)

# Projeto Teste: Extração de Trabalhos Artísticos #

### Objetivo ###

O objetivo deste teste é criar um web-scraper para extrair informações de trabalhos artísticos de um site de um museu.

**Nota:** Este site foi criado pelo ScrapingHUB a fim de testar web-scrapers. Tanto o site quanto este teste não possuem qualquer valor comercial.


### Desafio ###

Criar um web-scraper para coletar informações de todas as artes presentes nas categorias [Qing Japanese](http://pstrial-2019-12-16.toscrape.com/browse/qingjapanese) e [Une Tete](http://pstrial-2019-12-16.toscrape.com/browse/unetete).


O coletor deverá extrair cada arte(ex: http://pstrial-2019-12-16.toscrape.com/item/14879/Jacques_Tuboeuf) presente nas sub-categorias (ex: categoria qingjapanese: sub-categorias: Anne Joseph, And Miscellany, Of Grass ...).

Estes são os campos que esperamos que sejam extraídos:

* ID: (string) Identificação do arte 
* url: (string) URL da arte
* artistas: (lista de strings) Lista de artistas da arte (Fotógrafo, escultor, designer etc são considerados artistas)
* titulo: (string) Título da arte
* preco: (float) Valor da obra em BRL(Considere que o valor está em USD)
* imagem: (string) URL da imagem
* composicao: (lista de dicionários) Composições presentes na arte
* descricao: (string) Descrição da arte
* categorias: (lista de strings) Nomes das categorias de navegação que são necessárias para encontrar a arte. Ex: ["qingjapanese","annejoseph","annstreet"] [para estes projetos.](http://pstrial-2019-12-16.toscrape.com/browse/qingjapanese/annejoseph/annstreet)

### Começando

Este teste pode ser desenvolvido usando Scrapy([na qual esta documentação pode ser útil](https://doc.scrapy.org/en/latest/intro/tutorial.html#our-first-spider)) ou a própria estrutura presente neste repositório.


Além disso, dê uma olhada nos arquivos `decisoes.txt`,  `feedback.txt` e  `horas.txt`. 
A seção "Entregável" contém informações sobre estes arquivos.


#### Rodando Localmente
Por padrão, o coletor deve ser iniciado pelo arquivo `coletor_artemoderna/main.py`.


### Entregável ###

* O coletor de dados, em um repositório privado.

    O coletor deve ser escrito em python 3.8+ e seguir o padrão de código PEP8. Qualquer informação sensitiva deve ser removida do repositório.

    Por favor, mantenha os seguintes pontos em mente quando for entregar o teste:
    
    1. Histórico de Commit. Não se preocupe em entregar o histórico de commit limpo, faça quantos commits necessários como se estivesse trabalhando normalmente em um projeto. Nós usamos o histórico de commit para avaliar a evolução do seu trabalho, portanto, não faça commits com muitas modificações ao mesmo tempo.
    
    2. Qualidade de código. A versão final do seu código vai ser considerado como projeto concluído e como versão de produção. Por favor verifique se a execução do coletor de dados não apresenta falhas e se os resultados da coleta estão completos.

* Arquivo em .CSV ou .Parquet com todos os dados extraídos e devidamente tratados.
    


#### Invista tempo em criar um report

* Report de Horas

    Inclua um arquivo chamado "horas.txt" com uma lista de horas e tarefas no qual você investiu seu tempo. Você pode detalhar da forma como preferir, mas que seja sincero, resumido e objetivo. 
    Uma sugestão é usar o [serviço Clockfy](https://clockify.me/pt/), onde é possível ter um controle mais adequado de tarefas por hora e gerar um report bem bacana ao final do projeto.


* Report de Decisões
    
    Documente as decisões que você tomou ao longo do desenvolvimento em "decisoes.txt". Nós vamos nos referir à este arquivo caso seu código contenha pontos não atendam nossa expectativa.


* Report de Feedback

    Nós queremos receber um feedback deste teste. Adicione seu feedback no arquivo "feedback.txt". Sua opinião é muito importante para nós.

### Tempo Limite ###

Esperamos que esse teste dure entre 8 à 10 horas dependendo do seu nível de experiência.


Nós não queremos que este teste dure mais do que isso, então caso ultrapasse este limite, por favor considere alguns pontos importantes:


1. Priorizaremos o parsing dos dados. 

  Acreditamos que esta etapa é fundamental, então adicionamos um arquivo chamado `pages_to_scrape.parquet` presente em `coletor_artemoderna/assets/pages_to_scrape.parquet` que contém uma lista de todas as páginas que queremos que sejam extraídos os dados. 
  
  Caso não tenha tempo de desenvolver o coletor por completo, gostaremos que as informações de cada URL deste arquivo sejam devidamente extraídos e salvos em um arquivo csv único.
	
  2. Caso o parser esteja completo, mas alguma outra parte não esteja completa e o tempo de duração passou de 10 horas, pare o que está fazendo e finalize o teste com pelo menos os três reports completos.

### Data limite de entrega ###

Este teste não possui uma data limite de entrega, mas o quanto antes for entregue podemos ir para a próxima etapa do processo.
Não se esqueça de completar todos os entregáveis.

### Confidencialidade ###

Por favor não compartilhe este projeto ou crie posts em fóruns pela internet.
