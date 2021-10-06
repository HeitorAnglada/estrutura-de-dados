UFPA
Estrutura de dados
Problema do Carteiro Chines
Alunos: Caio Brasil - Alamario
        Heitor Anglada - heitormesk

O problema: 






A Solução:
      Caso o grafo seja euleriano, o menor percuso ou ciclo do carteiro será a soma dos pesos de todas as arestas, pois por ser euleriano, já será garantido a possibilidade de se percorrer todas as arestas uma única vez. Desse modo, no algorimo, caso todos os vértices sejam de grau par, o resultado será a soma de todas as arestas. Porém, caso seja trabalhado com grafos que possuem vertices com grau impar, o metodo será mais extenso.
      Primeiro, será necessário agrupar os vertices impares em um único conjunto a fim de encontrar o menor caminho entre esses vértices, por meio do algoritimo de Dijkstra. Após determninar. Após criar esse conjunto, deve ser selecionado qual o par de vertices de grau impar possui a menor distancia entre si, então será criado uma "nova " aresta entre esses dois vertices cujo o peso será essa menor distancia. Após isso, esses dois vertices serão removidos do conjunto dos vertices de grau impar, já que agora eles possuem grau par e esse processo de duplicação de arestas de menor caminho será repetido até que não aja mais vertices de grau impar.
      Então, como o novo grafo acaba possuindo todos os vértices de grau par, é possivel aplicar um algoritmo para resolução de grafos eulerianos, o que retornará o menor percurso que um "carteiro" deve percorrer pelas arestas assegurando que esse caminho seja o menor possivel. 

