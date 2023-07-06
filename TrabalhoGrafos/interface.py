import tkinter as tk
import tkinter.messagebox as messagebox
from kruskal import Grafo, algoritmo_kruskal
import networkx as nx # Biblioteca externa - Desenha o grafo
import matplotlib.pyplot as plt #Biblioteca externa - Exibe o grafo

def distancia(janela):
    # Cria uma janela com um plano de fundo azul claro
    janela_distancia = tk.Toplevel(janela) 
    janela_distancia.title("Defina as distancias das arestas")
    janela_distancia["bg"] = "lightblue"

    entrada_v1 = [] # Lista de entrada v1
    entrada_v2 = [] # Lista de entrada v2
    entrada_dist = [] # Lista de entrada de distância

    mensagem = tk.Label(janela_distancia, text="Insira a que vértices as arestas estão conectadas e sua distância", font=fonte)
    mensagem.grid(padx=10, pady=10, columnspan=6, sticky='n')
    mensagem["bg"] = "lightblue" # Define o plano de fundo de azul claro

    for i in range (1, num_arestas + 1):
        vertice_v1 = tk.Label(janela_distancia, text=f"Ponta V1 da Aresta {i}:", font=fonte)
        vertice_v1.grid(row=i, column=0, padx=10, pady=10)
        vertice_v1["bg"] = "lightblue" # Define o plano de fundo de azul claro

        campo_v1 = tk.Entry(janela_distancia)
        campo_v1.grid(row=i, column=1)
        entrada_v1.append(campo_v1) # Adição do texto à lista de entrada v1

        vertice_v2 = tk.Label(janela_distancia, text=f"Ponta V2 da Aresta {i}:", font=fonte)
        vertice_v2.grid(row=i, column=2, padx=10, pady=10)
        vertice_v2["bg"] = "lightblue"  # Define o plano de fundo de azul claro

        campo_v2 = tk.Entry(janela_distancia)
        campo_v2.grid(row=i, column=3)
        entrada_v2.append(campo_v2) # Adição do texto à lista de entrada v2

        dist = tk.Label(janela_distancia, text=f"Distância da Aresta {i}:", font=fonte)
        dist.grid(row=i, column=4, padx=10, pady=10)
        dist["bg"] = "lightblue"  # Define o plano de fundo de azul claro

        campo_dist = tk.Entry(janela_distancia)
        campo_dist.grid(row=i, column=5, padx=12)
        entrada_dist.append(campo_dist) # Adição do texto à lista de entrada de distância

    botao_inserir = tk.Button(janela_distancia, text="Inserir distancias", command=lambda: pre_kruskal(entrada_v1, entrada_v2, entrada_dist), bd=2, font=fonte_botao)
    botao_inserir.grid(row=num_arestas+1, columnspan=6, padx=10, pady=10)

def dados_grafos():
    global num_arestas
    global num_vertices
    
    # Verifica se os inputs da janela inicial estão com algum campo vazio
    if not entrada_vertices.get() or not entrada_arestas.get():
        messagebox.showerror("Erro", "Preencha todos os campos de entrada.")
    else:
        num_vertices = int(entrada_vertices.get()) # Transforma o número de vértices em inteiro e armazena na variável
        num_arestas = int(entrada_arestas.get()) # Transforma o número de arestas em inteiro e armazena na variável

        # Verifica se os valores nos inputs são menores ou igual a 0
        if num_vertices <= 0 or num_arestas <= 0:
            messagebox.showerror("Erro", "Número inválido. Insira um valor positivo para o número de vértices e arestas.")
        else:
            # Verifica se os valores estão dentro do padrão estabelecido para o programa
            if num_vertices >= 2 and num_arestas <= 12 and num_vertices <= 24 and num_arestas >= 1:
                distancia(janela)
            else:
                messagebox.showerror("Erro", "Quantia inválida. O número de vértices deve ser entre 2 e 24, e o de arestas entre 1 e 12")


def pre_kruskal(entrada_v1, entrada_v2, entrada_dist):
        grafo = Grafo(num_vertices) # Define um objeto 'grafo' do tipo Grafo que passa o número de vértices como parâmetro

        # Percorre "número de arestas" vezes para armazenar os elementos das listas de entrada em variáveis
        for i in range(num_arestas):
            try:
                v1 = int(entrada_v1[i].get()) - 1
                v2 = int(entrada_v2[i].get()) - 1
                dist = int(entrada_dist[i].get())
            except ValueError:
                # Tratamento de erro para o caso de valor inválido
                messagebox.showerror("Erro", "Valor inválido inserido.")

            grafo.adicionar_aresta(v1, v2, dist) # Adiciona as variáveis como parâmetros da função do grafo

        resultado = algoritmo_kruskal(grafo)

        tela_resultado(resultado, grafo)

def tela_resultado(resultado, grafo):
    # Cria um objeto de grafo do networkx
    grafo_desenho = nx.Graph()
    lista_arestas = grafo.arestas

    # Adiciona as arestas do grafo no objeto do grafo
    for aresta in lista_arestas:
        v1, v2, dist = aresta
        grafo_desenho.add_edge(v1, v2, weight=dist)

    # Cria uma lista com todas as arestas adicionadas
    todas_arestas = list(grafo_desenho.edges())

    # Exibe o grafo usando o matplotlib
    pos = nx.spring_layout(grafo_desenho)  # Layout do grafo
    campos = nx.get_edge_attributes(grafo_desenho, 'weight')  # Rótulos das arestas

    # Ajusta os índices dos nós no layout
    pos = {v: p for v, p in pos.items()}

    # Ajusta os rótulos dos nós para iniciar em '1'
    mapeamento_indices = {v: v + 1 for v in range(grafo.vertices)}

    nx.draw(grafo_desenho, pos, with_labels=False)  # Desenhar o grafo sem os rótulos

    # Desenha rótulos dos nós
    nx.draw_networkx_labels(grafo_desenho, pos, labels=mapeamento_indices, font_size=10, font_color='black')

    # Destaca os nós em vermelho
    nx.draw_networkx_nodes(grafo_desenho, pos, nodelist=mapeamento_indices.keys(), node_color='red', node_size=600)

    # Destaca as arestas do resultado em verde
    nx.draw_networkx_edges(grafo_desenho, pos, edgelist=resultado, edge_color='red', width=2.0)

    # Desenha rótulos das arestas
    nx.draw_networkx_edge_labels(grafo_desenho, pos, edge_labels=campos)

    # Desenha todas as arestas adicionadas em cinza claro
    nx.draw_networkx_edges(grafo_desenho, pos, edgelist=todas_arestas, edge_color='lightgray', width=1.0, alpha=0.5)

    plt.show()  # Exibe o gráfico

# Cria uma janela com um plano de fundo azul claro
janela = tk.Tk()
janela.title("Interface Gráfica")
janela["bg"] = "lightblue"

# Cria as variáveis que define a fonte, o tamanho e seu estado
fonte = ("Arial", 11, "bold")
fonte_botao = ("Arial", 8, "bold")

# Cria uma campo com mensagem escrita na janela e altera seu plano de fundo
grafo = tk.Label(janela, text="Programa auxiliador de decisões sobre o grafo para o prefeito!", font=fonte)
grafo.grid(padx=10, pady=10, sticky='n')
grafo["bg"] = "lightblue"

# Cria uma campo com mensagem escrita sobre vértices na janela e altera seu plano de fundo
texto_um = tk.Label(janela, text="Qual o número de vértices?", font=fonte)
texto_um.grid(row=1, padx=10, pady=10)
texto_um["bg"] = "lightblue"

# Define o campo de entrada (input) do número de vértices
entrada_vertices = tk.Entry(janela)
entrada_vertices.grid(row=2, padx=10, pady=5)

# Cria uma campo com mensagem escrita sobre arestas na janela e altera seu plano de fundo
texto_dois= tk.Label(janela, text="Qual o número de arestas?", font=fonte)
texto_dois.grid(row=3, padx=10, pady=10)
texto_dois["bg"] = "lightblue"

# Define o campo de entrada (input) do número de arestas
entrada_arestas = tk.Entry(janela)
entrada_arestas.grid(row=4, padx=10, pady=5)

# Botão que vai para a próxima janela para fornecer as conexões dos vértices, ou seja, as arestas
botao_distancia = tk.Button(janela, text="Inserir vértices e arestas", font=fonte_botao, command=dados_grafos, bd=2)
botao_distancia.grid(row=5, sticky="n", padx=10, pady=15)

janela.mainloop()