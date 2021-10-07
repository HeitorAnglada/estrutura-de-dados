from collections import defaultdict
'''Classe para representar o grafo'''
# representa o grafo
class Graph:
    def __init__(self):
        self.vertices = []
        self.arestas = defaultdict(list)
        self.visitadas = []
        self.custo = {}
        self.distancia = {}
        self.antecessores = {}
        self.impares = []

    # adiciona vertice
    def add_vertice(self, value):
        self.vertices.append(value)
        self.update_vertice_custo(value, float('inf'))

    # adiciona aresta
    def add_aresta(self, from_vertice, to_vertice, distance):
        self.arestas[from_vertice].append(to_vertice)
        self.distancia[(from_vertice, to_vertice)] = distance
        
    # visita vertice
    def visit_vertice(self, vertice):
        self.visitadas.append(vertice)

    # atualiza o custo do vertice 
    def update_vertice_custo(self, vertice, custo):
        self.custo.update({vertice: custo})
        
    # atualiza o custo dos antecessores
    def update_vertice_parent(self, vertice, parent):
        self.antecessores.update({vertice: parent})

    # retorna o vertice de menor custo  
    def encontra_menor_custo_vertice(self):
        menor_custo = float("inf")
        menor_custo_vertice = None

        for vertice in self.custo:
            custo = self.custo[vertice]

            if custo < menor_custo and vertice not in self.visitadas:
                menor_custo = custo
                menor_custo_vertice = vertice

        return menor_custo_vertice

    # retorna o grau de um vertice
    def grau_vertice(self, vertice):
        grau = 0
        for aresta in self.arestas.get(vertice):
            grau = grau + 1

        return grau

    # atualiza a lista 'impares' com todos os vertices de grau impar
    def graus_impar(self):
        for vertice in self.vertices:
            if self.grau_vertice(vertice) % 2 is not 0:
                self.impares.append(vertice)                                      
                
'''Funções'''

# encontra a menor distância entre dois pontos por meio do algorimo de dijkstra
def dijkstra(graph, inicial):
    # Definindo o custo 0 para o ponto inicial 
    graph.update_vertice_custo(inicial, 0)
    
    # Busca o menor vértice ainda não visitado
    vertice = graph.encontra_menor_custo_vertice()

    while vertice:
        # Recupera o custo desse vértice
        custo = graph.custo.get(vertice)
        
        # Recupera todas as arestas do vértice
        arestas = graph.arestas.get(vertice) if graph.arestas.get(vertice) else []
        
        for aresta in arestas:
            distance = graph.distancia.get((vertice, aresta))
            new_custo = custo + distance
            
            current_aresta_custo = graph.custo.get(aresta)

            # Para cada aresta, realiza a soma do custo com a distância e caso essa soma for menor que o custo atual, atualize o custo 
            if new_custo < current_aresta_custo:
                graph.update_vertice_custo(aresta, new_custo)
                graph.update_vertice_parent(aresta, vertice)

        # Marca o vértice como visitado
        graph.visit_vertice(vertice)
        
        # Busca o menor vértice ainda não visitado e continua o loop
        vertice = graph.encontra_menor_custo_vertice()

       
def enconta_menor_caminho(graph, vertice_to):
    to = vertice_to
    path = [to]
    
    while to:
        to = graph.antecessores.get(to)
        
        if not to:
            break
        
        path.append(to)

    path.reverse()

    return ' '.join(path)

def encontra_valor_menor_caminho(menor_caminho):
    menor_caminho = menor_caminho.split()
    dist = 0
    for x in range(len(menor_caminho)-1):
        dist = dist + graph.distancia[menor_caminho[x], menor_caminho[x+1]]

    return dist
       
'''Representando um grafo'''    

# inicia o grafo
graph = Graph()

# adiciona os vertices
graph.add_vertice('a')
graph.add_vertice('b')
graph.add_vertice('c')
graph.add_vertice('d')
graph.add_vertice('e')

# adiciona as arestas conectadas com o vertice 'a'
graph.add_aresta('a', 'b', 2)
graph.add_aresta('a', 'c', 4)
graph.add_aresta('a', 'd', 6)

# adiciona as arestas conectadas com o vertice 'b'
graph.add_aresta('b', 'a', 2)
graph.add_aresta('b', 'd', 3)
graph.add_aresta('b', 'e', 7)

# adiciona as arestas conectadas com o vertice 'c'
graph.add_aresta('c', 'a', 4)
graph.add_aresta('c', 'e', 9)

# adiciona as arestas conectadas com o vertice 'c'
graph.add_aresta('d', 'a', 6)
graph.add_aresta('d', 'b', 3)
graph.add_aresta('d', 'e', 1)

# adiciona as arestas conectadas com o vertice 'e'
graph.add_aresta('e', 'b', 7)
graph.add_aresta('e', 'c', 9)
graph.add_aresta('e', 'd', 1)

# preenche o atributo 'impares' com todos vertices de grau impar
graph.graus_impar()    
    
'''Processamento'''

# verifica de há vertices de grau impar
if len(graph.impares) == 0:  # se o grafo não tem vertices de grau impar é um grafo euleriano portanto basta somar as suas arestas
    distancia=0
    
    for aresta in graph.distancia.values():
        distancia = distancia + aresta
    distancia = distancia/2  #divide por 2 pois cada aresta é declarada duas vezes visto que ela é declarada para o ponto inicial e o final
    print(f"A distância mínima a ser percorrida é {distancia}")

'''
se o grafo tem vertices de grau impar ele é um grafo não euleriano portanto deve-se aplicar o algorimo de dijkstra nesses vertices, dois a dois afim
 de encontrar os menores caminhos caminhos entre eles para duplica-los e então gerar artificialmente um grafo euleriano que tera suas arestas somadas
 e assim o menor percurso será encontrado
'''

else:
    menor_distancia = float('inf')
    menor_caminho = []
    caminho_atual = []
    lista_caminho_atual = []

    # encontra a distancia do vertice x para todos os outros e guarda a menor
    for x in graph.impares:
        distancia = float('inf')
        
        for vertice2 in graph.impares:
           
            if distancia < menor_distancia and distancia != 0:
                menor_distancia = distancia
                menor_caminho = caminho_atual
                distancia = 0
            else:
                distancia = 0
    
            if x == vertice2:
                pass
    
            else:
                dijkstra(graph, x)
                caminho_atual = enconta_menor_caminho(graph, vertice2)
                distancia = encontra_valor_menor_caminho(caminho_atual)
                
                
        
    
        
              
        
