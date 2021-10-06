UFPA
Estrutura de dados
Problema do Carteiro Chines
Alunos: Caio Brasil - Alamario
        Heitor Anglada - heitormesk
        Gabriel Ribeiro - Gabrielsr10

O problema: 
        Em teoria dos grafos, o Problema do Carteiro Chinês (PCC), caracteriza-se pela roteirização de arcos e tem como objetivo a cobertura de arcos de um grafo, criando uma rota que passe ao menos uma vez em cada um destes arcos.
        Em resumo, consiste em encontrar um caminho mais curto ou circuito fechado que visite cada aresta de um grafo não direcionado.
        Alan Goldman do U.S. National Bureau of Standards deu pela primeira vez o nome 'Problema do Carteiro Chinês' para este problema, pois, foi originalmente estudado pelo matemático chinês Mei-Ku Kuan em 1962.
        Considerando: Os pontos representando as casas de uma cidade, e as linhas os caminhos entre as casas. Se um carteiro tem que visitar cada uma das casas entregando suas cartas, o ideal seria que ele passasse uma única vez por cada caminho e retornasse ao ponto de origem. Quando esse problema é levado para a Teoria dos Grafos é possível descrever as possíveis soluções e propor os melhores caminhos para o carteiro.

A Solução:
      Caso o grafo seja euleriano, o menor percuso ou ciclo do carteiro será a soma dos pesos de todas as arestas, pois por ser euleriano, já será garantido a possibilidade de se percorrer todas as arestas uma única vez. Desse modo, no algorimo, caso todos os vértices sejam de grau par, o resultado será a soma de todas as arestas. Porém, caso seja trabalhado com grafos que possuem vertices com grau impar, o metodo será mais extenso.
      Primeiro, será necessário agrupar os vertices impares em um único conjunto a fim de encontrar o menor caminho entre esses vértices, por meio do algoritimo de Dijkstra. Após determninar. Após criar esse conjunto, deve ser selecionado qual o par de vertices de grau impar possui a menor distancia entre si, então será criado uma "nova " aresta entre esses dois vertices cujo o peso será essa menor distancia. Após isso, esses dois vertices serão removidos do conjunto dos vertices de grau impar, já que agora eles possuem grau par e esse processo de duplicação de arestas de menor caminho será repetido até que não aja mais vertices de grau impar.
      Então, como o novo grafo acaba possuindo todos os vértices de grau par, é possivel aplicar um algoritmo para resolução de grafos eulerianos, o que retornará o menor percurso que um "carteiro" deve percorrer pelas arestas assegurando que esse caminho seja o menor possivel. 
      
Aplicação do PCC:


