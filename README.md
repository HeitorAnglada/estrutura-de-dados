# UFPA-Estrutura de dados
## Problema do Carteiro Chines
### Alunos: Caio Brasil - Alamario
###        Heitor Anglada - heitormesk
###        Gabriel Ribeiro - Gabrielsr10
###        Daniel Campos - Daniellcampos7

# O problema: 
   Em teoria dos grafos, o Problema do Carteiro Chinês (PCC), caracteriza-se pela roteirização de arcos e tem como objetivo a cobertura de arcos de um grafo, criando uma rota que passe ao menos uma vez em cada um destes arcos.
        Em resumo, consiste em encontrar um caminho mais curto ou circuito fechado que visite cada aresta de um grafo não direcionado.
        Alan Goldman do U.S. National Bureau of Standards deu pela primeira vez o nome 'Problema do Carteiro Chinês' para este problema, pois, foi originalmente estudado pelo matemático chinês Mei-Ku Kuan em 1962.
        Considerando: Os pontos representando as casas de uma cidade, e as linhas os caminhos entre as casas. Se um carteiro tem que visitar cada uma das casas entregando suas cartas, o ideal seria que ele passasse uma única vez por cada caminho e retornasse ao ponto de origem. Quando esse problema é levado para a Teoria dos Grafos é possível descrever as possíveis soluções e propor os melhores caminhos para o carteiro.

# A Solução:
   Caso o grafo seja euleriano, o menor percuso ou ciclo do carteiro será a soma dos pesos de todas as arestas, pois por ser euleriano, já será garantido a possibilidade de se percorrer todas as arestas uma única vez. Desse modo, no algorimo, caso todos os vértices sejam de grau par, o resultado será a soma de todas as arestas. Porém, caso seja trabalhado com grafos que possuem vertices com grau impar, o metodo será mais extenso.
      Primeiro, será necessário agrupar os vertices impares em um único conjunto a fim de encontrar o menor caminho entre esses vértices, por meio do algoritimo de Dijkstra. Após determninar. Após criar esse conjunto, deve ser selecionado qual o par de vertices de grau impar possui a menor distancia entre si, então será criado uma "nova " aresta entre esses dois vertices cujo o peso será essa menor distancia. Após isso, esses dois vertices serão removidos do conjunto dos vertices de grau impar, já que agora eles possuem grau par e esse processo de duplicação de arestas de menor caminho será repetido até que não aja mais vertices de grau impar.
      Então, como o novo grafo acaba possuindo todos os vértices de grau par, é possivel aplicar um algoritmo para resolução de grafos eulerianos, o que retornará o menor percurso que um "carteiro" deve percorrer pelas arestas assegurando que esse caminho seja o menor possivel. 
      
# Aplicação do PCC:
Uma aplicação do PCC é direcionado na coleta de lixo urbano.                         
       Otimizar rotas para caminhões de lixo urbano contribuem para a redução de custos dos cofres públicos. Este trabalho objetiva apresentar um programa simples para resolução do Problema do Carteiro Chinês Direcionado atuando na determinação de rotas mínimas para veículos coletores de lixo e aplicado em dois bairros na cidade de Recife-PE. 
       O programa recebe a matriz de distâncias do grafo e determina a rota ótima em 3 etapas: escrever o modelo matemático que resolve o PCCD, resolvê-lo por um solver e traçar a rota em um grafo Euleriano. O resultado do programa foi comparado com as rotas atuais: redução da distância total de 12,7% no bairro (Engenho do Meio) e 8,86% no bairro (Cordeiro). O tour para o caminhão de lixo obteve redução na distância total, embora algumas ruas precisassem ser percorridas mais de uma vez para alcançar certos segmentos de ruas, ainda assim garantiu melhor solução do que a rota atual.

# Explicando O Código
   Primeiramente o código inicia com uma clasee para representar um grafo. 
   
   ![image](https://user-images.githubusercontent.com/60029072/136312015-6f3b4f64-78e3-4cfc-8349-22a6b8728011.png)
   
   Em seguida está um exemplo de representação do grafo abaixo.
   
   ![image](https://user-images.githubusercontent.com/60029072/136311310-1364109a-2eb9-48ef-bda7-d6ea4e945054.png)

   Para representa-lo é necessário seguir os seguintes passos:
   
   #### 1. Inicializar o grafo
   
   ![image](https://user-images.githubusercontent.com/60029072/136311104-87ad018a-f3ec-4392-927a-de9219378ca4.png)
   
   #### 2. Declarar seus vertices
   
   ![image](https://user-images.githubusercontent.com/60029072/136311214-08e8b3bf-3118-4690-91a6-3f5dda538ead.png)
   
   #### 3. Atribuir para cada um dos seus vertices as suas ramificações e os valores das mesmas
   
   ![image](https://user-images.githubusercontent.com/60029072/136311752-594bf194-6a85-4603-8d44-3930ca3fafca.png)
   
   #### 4. Escrever o comando abaixo para criar uma lista com todos os vertices de grau impar
   
   ![image](https://user-images.githubusercontent.com/60029072/136311880-2e00c309-0240-4933-867e-6342d61cc6a8.png)


   Para solucionar o problema do Carteiro Chinês nos primeiramente precisamos definir se o grafo é ou não euleriano. Para tal foi usado o código abaixo, que verifica se a lista de vertices impares gerada anteriormente tem algum item. Se estiver vazia o grafico é euleriano.
   
   ![image](https://user-images.githubusercontent.com/60029072/136312287-d2835d46-aaf7-490a-929a-f89078253162.png)
   
   No caso do grafo ser euleriano basta somar o valor de suas arestas, mas no nosso tivemos que dividir por 2 pois cada aresta é declarada duas vezes tendo em vista que arestas conectam 2 vertices e cada vertice devra declarar esta aresta como no trecho de código abaixo.
   
   ![image](https://user-images.githubusercontent.com/60029072/136312769-1bab361d-b1a2-4968-8cda-eb61350c522d.png)

   Por outro lado se o grafo tem vertices de grau impar ele é um grafo não euleriano portanto deve-se aplicar o algorimo de dijkstra, como o exemplificado abaixo, nesses vertices, dois a dois afim de encontrar os menores caminhos entre eles para duplica-los e então gerar artificialmente um grafo euleriano que tera suas arestas somadas
 e assim o menor percurso será encontrado.
 
 ![image](https://user-images.githubusercontent.com/60029072/136313296-45866091-de6a-40dd-adb7-27a6c065bd4c.png)





   



