# -*- coding: UTF-8 -*-
#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Nov 05, 2017 08:11:42 PM
import sys
import tkinter
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import numpy as np
import re
import random as rd


class Path:
    def __init__(self, grafo, n, qtd_chamadas):
        # Exemplo de execução - Substitua o grafo pelo oq vc vai passar
        if len(grafo) == 0: pass
            #"b":{"f":{'peso': 80, 'lamda':[f, f, f, f, f,...,n]}, "g":900},
        '''self.grafo = {"a":{"c":{"peso":100, "labd":[False for i in range(n)]}, "f":{"peso":90, "labd":[False for i in range(n)]}, "g":{"peso":100, "labd":[False for i in range(n)]}, "l":{"peso":120, "labd":[False for i in range(n)]}, "n":{"peso":150, "labd":[False for i in range(n)]}},
    "b":{"f":{"peso":80, "labd":[False for i in range(n)]}, "g":{"peso":90, "labd":[False for i in range(n)]}},
    "c":{"a":{"peso":100, "labd":[False for i in range(n)]}, "d":{"peso":60, "labd":[False for i in range(n)]}},
    "d":{"c":{"peso":60, "labd":[False for i in range(n)]}, "n":{"peso":110, "labd":[False for i in range(n)]}},
    "e":{"f":{"peso":100, "labd":[False for i in range(n)]}, "n":{"peso":100, "labd":[False for i in range(n)]}},
    "f":{"a":{"peso":90, "labd":[False for i in range(n)]}, "b":{"peso":80, "labd":[False for i in range(n)]}, "e":{"peso":100, "labd":[False for i in range(n)]}, "h":{"peso":140, "labd":[False for i in range(n)]}, "p":{"peso":100, "labd":[False for i in range(n)]}, "q":{"peso":100, "labd":[False for i in range(n)]}},
    "g":{"a":{"peso":100, "labd":[False for i in range(n)]}, "b":{"peso":90, "labd":[False for i in range(n)]}, "h":{"peso":120, "labd":[False for i in range(n)]}, "i":{"peso":90, "labd":[False for i in range(n)]}, "q":{"peso":100, "labd":[False for i in range(n)]}},
    "h":{"f":{"peso":140, "labd":[False for i in range(n)]}, "g":{"peso":120, "labd":[False for i in range(n)]}},
    "i":{"g":{"peso":90, "labd":[False for i in range(n)]}, "r":{"peso":90, "labd":[False for i in range(n)]}},
    "j":{"l":{"peso":150, "labd":[False for i in range(n)]}, "r":{"peso":90, "labd":[False for i in range(n)]}},
    "l":{"a":{"peso":120, "labd":[False for i in range(n)]}, "j":{"peso":150, "labd":[False for i in range(n)]}},
    "m":{"n":{"peso":100, "labd":[False for i in range(n)]}, "o":{"peso":100, "labd":[False for i in range(n)]}},
    "n":{"a":{"peso":150, "labd":[False for i in range(n)]}, "d":{"peso":110, "labd":[False for i in range(n)]}, "e":{"peso":100, "labd":[False for i in range(n)]}, "m":{"peso":100, "labd":[False for i in range(n)]}},
    "o":{"m":{"peso":100, "labd":[False for i in range(n)]}, "p":{"peso":90, "labd":[False for i in range(n)]}},
    "p":{"f":{"peso":100, "labd":[False for i in range(n)]}, "o":{"peso":90, "labd":[False for i in range(n)]}},
    "q":{"f":{"peso":100, "labd":[False for i in range(n)]}, "g":{"peso":100, "labd":[False for i in range(n)]}},
    "r":{"i":{"peso":90, "labd":[False for i in range(n)]}, "j":{"peso":90, "labd":[False for i in range(n)]}}}'''
        self.grafo = grafo
        self.gerar_simulacoes(qtd_chamadas, self.grafo)
        self.first_fit(self.grafo, 'simulação_'+str(qtd_chamadas)+'.txt')
            
    def dijkstra(self, grafo, origem, fim):
        controle = { }
        distanciaAtual = { }
        noAtual = { }
        naoVisitados = []
        atual = origem
        noAtual[atual] = 0
        aux = []
    
        
        for vertice in grafo.keys():
            naoVisitados.append(vertice)   
            distanciaAtual[vertice] = float('inf')
    
        distanciaAtual[atual] = [0,origem] 
    
        naoVisitados.remove(atual)
    
        while naoVisitados:
            for vizinho, item in grafo[atual].items():
                # print(item)
                peso = item['peso']
                pesoCalc = peso + noAtual[atual]
                if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho][0] > pesoCalc:
                    distanciaAtual[vizinho] = [pesoCalc, atual]
                    controle[vizinho] = pesoCalc
                     
            if controle == {} : break    
            minVizinho = min(controle.items(), key=lambda x: x[1])
            atual=minVizinho[0]
            noAtual[atual] = minVizinho[1]
            naoVisitados.remove(atual)
            del controle[atual]
        aux.append(self.rota(distanciaAtual, origem, fim))
        return re.sub('[^a-zA-Z0-9 \\\]', '', str(aux)).split(), distanciaAtual[fim][0]


    def rota(self, distancias,inicio, fim):
        if  fim != inicio:
            return self.rota(distancias,inicio, distancias[fim][1]), fim
        else:
            return inicio


    def encontrar_todos_caminhos(self, grafo, origem, destino, path=[]):
        path = path + [origem]
        
        if origem == destino:
            return [path]
       	     
        if origem not in grafo:
            return []
        
        paths = []
        for vertice in list(grafo[origem].keys()):
            if vertice not in path:
                extended_paths = self.encontrar_todos_caminhos(grafo, vertice, destino, path)
                for p in extended_paths: 
                    paths.append(p)
        return paths


    def gerar_simulacoes(self, qnt_simu, grafo):
        path = 'simulação_' + str(qnt_simu) + '.txt'
        file_simu = open(path,'w')
    
        caracters = []
    
        for key, item in grafo.items():
            caracters.append(key)
    
        for i in range(qnt_simu):
            origem, destino = rd.sample(caracters, 2)
            caminho_minimo, custo = self.dijkstra(grafo, origem, destino)
            s = origem  + ' -> ' + destino + ' = ' + str(custo) + ' : '
            for i in caminho_minimo:
                s += i + ' --> '
            s = s[:-5]
            s+='\n'
            file_simu.writelines(s)
    
        file_simu.close()
    
    
        file_simu = open(path,'r')
        file_all = open('caminho_all_' + str(qnt_simu) + '.txt','w')
    
        for line in file_simu:
            origem, destino = line[0], line[5]
            lista_todos_caminho = self.encontrar_todos_caminhos(grafo, origem, destino)
            s = '#' + origem + ' -> ' + destino + '\n'
            for i in lista_todos_caminho:
                k = 0
                soma = 0
                while k != len(i)-1:
                    soma += grafo[i[k]][i[k+1]]['peso']
                    k+=1
                for j in i:
                    s += j + ' --> '
                s = s[:-5]
                s+= ' ' + str(soma) + '\n'
            file_all.writelines(s)
        file_all.close()


    def first_fit(self, grafo, path_chamadas_grafo):
        block = 0
        with open(path_chamadas_grafo,"r") as file:
            data = file.readlines()
            size_call = len(data)

            for line in data:
                path = line.strip()
                path = path.split(':')[1].split(' ')[1:]
                path = [path[i] for i in range(0,len(path),2)]
                
                accept = False
                position = 0

                while accept == False:
                    accept = True
                    for i in range(len(path) -1):
                        origem, destino = path[i], path[i+1]
                        if  grafo[origem][destino]['lambda'][position] == True and grafo[destino][origem]['lambda'][position] == True:
                            accept = False
                            position += 1
                            break
                    if position == len(grafo[path[0]][path[1]]['lambda']) - 1:
                        block += 1
                    
                        break

                if accept:
                    for i in range(len(path) -1):
                        origem, destino = path[i], path[i+1]
                        grafo[origem][destino]['lambda'][position] = True
                        grafo[destino][origem]['lambda'][position] = True
        
        file = open('block_'+str(size_call)+ '_' + str(len(grafo[path[0]][path[1]]['lambda'])) +'.txt','w')
        print("ok")
        print('Número de chamadas: ' + str(size_call) + '\n')
        print('Taxa de bloqueio: ' + str(float(block)/10))
        print('Comprimento de onde: ' + str(len(grafo[path[0]][path[1]]['lambda'])) + '\n')
        file.writelines('Número de chamadas: ' + str(size_call) + '\n')
        file.writelines('Comprimento de onde: ' + str(len(grafo[path[0]][path[1]]['lambda'])) + '\n')
        file.writelines('Número de bloqueios: ' + str(block) + '\n')
        file.writelines('Taxa de bloqueio: ' + str(float(block)/10))
        file.close()

class Aresta:
    def __init__(self, canvas):
        self.no_origem = None
        self.no_destino = None
        self._lambda = 20
        self.peso = np.inf
        self.canvas = canvas
        self.label = Label(canvas)
        self.objeto = None

    def set_origem(self, no_origem):
        self.no_origem = no_origem

    def set_destino(self, no_destino):
        print("destino")
        self.no_destino = no_destino
        self.objeto = self.canvas.create_line(self.no_origem.pos[0] + 25, self.no_origem.pos[1] + 25,
                                              self.no_destino.pos[0] + 25, self.no_destino.pos[1] + 25,
                                              width=3, fill='black')
        x_medio = (self.no_origem.pos[0] + 25 + self.no_destino.pos[0]) / 2
        y_medio = (self.no_origem.pos[1] + 25 + self.no_destino.pos[1]) / 2
        self.label.place(x=x_medio, y=y_medio)
        self.label.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text=self.peso)
        self.label.bind("<Double-Button-1>", self.set_peso)

    def set_peso(self, event):
        aux = tkinter.Toplevel()

        aux.geometry("170x150+417+160")
        aux.title("Aresta")
        aux.configure(background="#d9d9d9")

        lbl_edge_peso = Label(aux)
        lbl_edge_peso.place(relx=0.01, rely=0.13)
        lbl_edge_peso.configure(text="Peso", background="#d9d9d9")

        txt_edge_peso = Entry(aux)
        txt_edge_peso.place(relx=0.29, rely=0.13, width=100)
        txt_edge_peso.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                foreground="#000000", insertbackground="black", width=124)

        lbl_edge_lambda = Label(aux)
        lbl_edge_lambda.place(relx=0.01, rely=0.33)
        lbl_edge_lambda.configure(text="Lambda", background="#d9d9d9")

        txt_edge_lambda = Entry(aux)
        txt_edge_lambda.place(relx=0.29, rely=0.33, width=100)
        txt_edge_lambda.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                foreground="#000000", insertbackground="black", width=124)

        btn_set_edge_peso = Button(aux)
        btn_set_edge_peso.place(relx=0.29, rely=0.53)
        btn_set_edge_peso.configure(activebackground="#d9d9d9", activeforeground="#000000", background="#d9d9d9",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", pady="0", text="Confirmar")

        txt_edge_peso.focus()
        txt_edge_peso.bind("<Return>", lambda event: self.salvar_peso(txt_edge_peso.get(), txt_edge_lambda.get(), aux))
        btn_set_edge_peso.bind("<Button-1>", lambda event: self.salvar_peso(txt_edge_peso.get(),  txt_edge_lambda.get(), aux))


    def salvar_peso(self, peso, _lambda, window):
        self.peso = peso
        self._lambda = _lambda
        self.label.configure(text=self.peso)
        window.destroy()


class No:
    def __init__(self, event, canvas, imagem):
        self.mat_no = []
        for i in range(event.x-25, event.x+25):
            aux = []
            for j in range(event.y-25, event.y+25):
                aux.append((i, j))
            self.mat_no.append(aux)
        self.image = imagem
        self.canvas = canvas
        self.nome = 'Empty'
        self.pos = (event.x-25, event.y-25)
        self.label = Label(canvas)
        self.label.place(x=self.pos[0] + 3, y=self.pos[1] - 13)
        self.label.configure(background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000", text=self.nome)
        self.objeto = self.canvas.create_image(self.pos, image=self.image, anchor='nw', tags=self.nome)

        self.canvas.tag_bind(self.objeto, "<Double-Button-1>", self.set_nome)
        self.canvas.unbind("<Button-1>")

    def set_nome(self, event):
        aux = tkinter.Toplevel()

        aux.geometry("207x75+417+160")
        aux.title("NOME")
        aux.configure(background="#d9d9d9")

        txt_node_name = Entry(aux)
        txt_node_name.place(relx=0.19, rely=0.13, relheight=0.27, relwidth=0.6)
        txt_node_name.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                foreground="#000000", insertbackground="black", width=124)

        btn_set_node_name = Button(aux)
        btn_set_node_name.place(relx=0.39, rely=0.53)
        btn_set_node_name.configure(activebackground="#d9d9d9", activeforeground="#000000", background="#d9d9d9",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", pady="0", text="Confirmar")

        txt_node_name.focus()
        txt_node_name.bind("<Return>", lambda event: self.salvar_nome(txt_node_name.get(), aux))
        btn_set_node_name.bind("<Button-1>", lambda event: self.salvar_nome(txt_node_name.get(), aux))

    def salvar_nome(self, nome, window):
        self.nome = nome
        self.label.configure(text=self.nome)
        window.destroy()


class Grafo:
    def __init__(self):
        self.lista_nos = []
        self.lista_arestas = []
        self.matriz_ajd = None
        self.lista_adj = None

    def set_lambdas(self, _lambda):
        for aresta in self.lista_arestas:
            aresta._lambda = int(_lambda)

    def set_matriz(self):
        self.matriz_ajd = [[None for i in range(0, len(self.lista_nos))] for j in range(0, len(self.lista_nos))]
        #self.matriz_ajd = np.matrix(np.ones((len(self.lista_nos), len(self.lista_nos))) * np.inf)
        for aresta in self.lista_arestas:
            origem = self.lista_nos.index(aresta.no_origem)
            destino = self.lista_nos.index(aresta.no_destino)
            self.matriz_ajd[origem][destino] = aresta
            self.matriz_ajd[destino][origem] = aresta

    def set_lista(self):
        self.lista_adj = {}
        for i in range(0, len(self.matriz_ajd)):
            aux = {}
            for j in range(0, len(self.matriz_ajd)):
                if self.matriz_ajd[i][j] != None:
                    aux2 = {}
                    aux2['peso'] = int(self.matriz_ajd[i][j].peso)
                    aux2['lambda'] = [False for i in range(0, self.matriz_ajd[i][j]._lambda)]
                    aux[self.lista_nos[j].nome] = aux2
            self.lista_adj[self.lista_nos[i].nome] = aux

    def get_grafo(self):
        self.set_matriz()
        self.set_lista()
        grafo = ''
        grafo += '--------------------VERTICES--------------------\n'
        for i in range(0, len(self.lista_nos)):
            grafo += str(i) + ': ' + self.lista_nos[i].nome + '\n'

        grafo += '\n---------------------ARESTAS--------------------\n'
        for i in range(0, len(self.lista_arestas)):
            grafo += self.lista_arestas[i].no_origem.nome + ' -> ' + self.lista_arestas[i].no_destino.nome + ' = ' + str(self.lista_arestas[i].peso) + ' -' \
                                                                                                                                                       ' ' + str(self.lista_arestas[i]._lambda) + '\n'

        grafo += '\n----------------------GRAFO---------------------\n'
        dic = '{'
        for i in range(0, len(self.matriz_ajd)):
            dic += self.lista_nos[i].nome + ': '
            aux = '{'
            for j in range(0, len(self.matriz_ajd)):
                if self.matriz_ajd[i][j] != None:
                    aux += self.lista_nos[j].nome + ':{peso:' + str(self.matriz_ajd[i][j].peso) + ', lambda:'+str(self.matriz_ajd[i][j]._lambda)+'}, '
            aux = aux[0:len(aux)-2]
            aux += '},\n'
            dic += aux
        dic = dic[0:len(dic)-2]
        dic += '}'
        grafo += dic

        return grafo

class Simulador:
    def __init__(self, top=None):
        global op_dijkstra
        op_dijkstra = BooleanVar()
        self.no_origem = None
        self.no_destino = None
        self.g = Grafo()
        self.top = top
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self._bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        self._fgcolor = '#000000'  # X11 color: 'black'
        self._compcolor = '#d9d9d9' # X11 color: 'gray85'
        self._ana2color = '#d9d9d9' # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32": self.style.theme_use('winnative')
        self.style.configure('.', background=self._bgcolor)
        self.style.configure('.', foreground=self._fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', self._compcolor), ('active',self._ana2color)])

        self.top.geometry("1240x640+0+0")
        self.top.title("Simulador")
        self.top.configure(background="#d9d9d9")

        self.menu_bar = tkinter.Menu(self.top)
        self.menu_file = tkinter.Menu(self.menu_bar, tearoff=0)
        self.menu_file.add_command(label="Novo", command=self.novo)
        self.menu_file.add_command(label="Abrir", command=self.passing)
        self.menu_file.add_command(label="Salvar", command=self.passing)
        self.menu_file.add_command(label="Salvar como...", command=self.passing)
        self.menu_file.add_separator()
        self.menu_file.add_command(label="Sair", command=self.top.destroy)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.menu_file)
        top.config(menu=self.menu_bar)

        self.imagem = PhotoImage(file='node.png')
        self.top.imagem = self.imagem
        
    def passing(self):
        pass

    def novo(self):

        self.style.configure('TNotebook.Tab', background=self._bgcolor)
        self.style.configure('TNotebook.Tab', foreground=self._fgcolor)
        self.style.map('TNotebook.Tab', background=[('selected', self._compcolor), ('active',self._ana2color)])
        self.nb = ttk.Notebook(self.top)
        self.nb.place(relx=0.0, rely=0.0, relheight=1.01, relwidth=1.0)
        self.nb.configure(width=824)
        self.nb.configure(takefocus="")
        self.fr_topologia = ttk.Frame(self.nb)
        self.nb.add(self.fr_topologia, padding=3)
        self.nb.tab(0, text="Topologia",underline="-1",)
        self.fr_configuracoes = ttk.Frame(self.nb)
        self.nb.add(self.fr_configuracoes, padding=3)
        self.nb.tab(1, text="Configurações",underline="-1",)
        self.fr_saida = ttk.Frame(self.nb)
        self.nb.add(self.fr_saida, padding=3)
        self.nb.tab(2, text="Saída",underline="-1",)
        self.fr_simular = ttk.Frame(self.nb)
        self.nb.add(self.fr_simular, padding=3)
        self.nb.tab(3, text="Simular",underline="-1",)

        """
        ABA TOPOLOGIA
        """
        self.btn_no = ttk.Button(self.fr_topologia)
        self.btn_no.place(relx=0.01, rely=0.02, height=25, width=106)
        self.btn_no.configure(takefocus="")
        self.btn_no.configure(text='''Nó''')
        self.btn_no.configure(width=106)

        self.btn_aresta = ttk.Button(self.fr_topologia)
        self.btn_aresta.place(relx=0.17, rely=0.02, height=25, width=106)
        self.btn_aresta.configure(takefocus="")
        self.btn_aresta.configure(text='''Aresta''')
        self.btn_aresta.configure(width=106)

        self.desenho_topologia = Canvas(self.fr_topologia)
        self.desenho_topologia.place(relx=0.01, rely=0.08, relheight=0.91, relwidth=0.98)
        self.desenho_topologia.configure(background="white")
        self.desenho_topologia.configure(borderwidth="2")
        self.desenho_topologia.configure(insertbackground="black")
        self.desenho_topologia.configure(relief=RIDGE)
        self.desenho_topologia.configure(selectbackground="#c4c4c4")
        self.desenho_topologia.configure(selectforeground="black")
        self.desenho_topologia.configure(width=806)

        """
        NOTEBOOK CONFIGURAÇÕES
        """
        self.nb2 = ttk.Notebook(self.fr_configuracoes)
        self.nb2.place(relx=0.0, rely=0.0, relheight=0.99, relwidth=0.99)
        self.nb2.configure(width=814)
        self.nb2.configure(takefocus="")
        self.fr_algoritmos = ttk.Frame(self.nb2)
        self.nb2.add(self.fr_algoritmos, padding=3)
        self.nb2.tab(0, text="Algoritmos",underline="-1",)
        self.fr_chamadas = ttk.Frame(self.nb2)
        self.nb2.add(self.fr_chamadas, padding=3)
        self.nb2.tab(1, text="Chamadas", underline="-1", )
        """
        self.fr_origem_destino = ttk.Frame(self.nb2)
        self.nb2.add(self.fr_origem_destino, padding=3)
        self.nb2.tab(2, text="Orig. -> Dest.", underline="-1",)
        """
        """
        ABA CONFIGURAÇÕES -> ABA ALGORITMOS
        """
        self.chk_dijkstra = ttk.Checkbutton(self.fr_algoritmos)
        self.chk_dijkstra.place(relx=0.01, rely=0.02, relwidth=0.08, relheight=0.0, height=21)
        self.chk_dijkstra.configure(variable=op_dijkstra)
        self.chk_dijkstra.configure(takefocus="")
        self.chk_dijkstra.configure(text='''Dijkstra''')
        """
        ABA CONFIGURAÇÕES -> ABA CHAMADAS
        """
        self.lbl_num_chamadas = ttk.Label(self.fr_chamadas)
        self.lbl_num_chamadas.place(relx=0.01, rely=0.02, relwidth=0.16)
        self.lbl_num_chamadas.configure(text="Número de chamadas")
        self.txt_num_chamadas = ttk.Entry(self.fr_chamadas)
        self.txt_num_chamadas.place(relx=0.15, rely=0.02)

        self.lbl_lambda = ttk.Label(self.fr_chamadas)
        self.lbl_lambda.place(relx=0.01, rely=0.12, relwidth=0.16)
        self.lbl_lambda.configure(text="Comprimentos de onda")
        self.txt_lambda = ttk.Entry(self.fr_chamadas)
        self.txt_lambda.place(relx=0.15, rely=0.12)

        """
        ABA SAÍDA
        """
        self.fr_salvar = ttk.Frame(self.fr_saida)
        self.fr_salvar.place(relx=0.01, rely=0.02, relheight=0.26, relwidth=0.23)

        self.fr_salvar.configure(relief=GROOVE)
        self.fr_salvar.configure(borderwidth="2")
        self.fr_salvar.configure(relief=GROOVE)
        self.fr_salvar.configure(width=185)

        self.lbl_salvar = ttk.Label(self.fr_salvar)
        self.lbl_salvar.place(relx=0.11, rely=0.07, height=19, width=142)
        self.lbl_salvar.configure(background="#d9d9d9")
        self.lbl_salvar.configure(foreground="#000000")
        self.lbl_salvar.configure(relief=FLAT)
        self.lbl_salvar.configure(text='''Escolha o local do arquivo''')

        self.lbl_local = ttk.Label(self.fr_salvar)
        self.lbl_local.place(relx=0.05, rely=0.3, height=19, width=32)
        self.lbl_local.configure(background="#d9d9d9")
        self.lbl_local.configure(foreground="#000000")
        self.lbl_local.configure(relief=FLAT)
        self.lbl_local.configure(text='''Local''')

        self.txt_local = ttk.Entry(self.fr_salvar)
        self.txt_local.place(relx=0.27, rely=0.3, relheight=0.16, relwidth=0.68)
        self.txt_local.configure(takefocus="")
        self.txt_local.configure(cursor="ibeam")

        self.btn_salvar = ttk.Button(self.fr_salvar)
        self.btn_salvar.place(relx=0.27, rely=0.59, height=25, width=76)
        self.btn_salvar.configure(takefocus="")
        self.btn_salvar.configure(text='''Salvar''')
        self.btn_salvar.configure(command=self.g.set_matriz)

        """
        ABA SIMULAR
        """
        self.btn_simular = ttk.Button(self.fr_simular)
        self.btn_simular.place(relx=0.01, rely=0.02, height=25, width=106)
        self.btn_simular.configure(takefocus="")
        self.btn_simular.configure(text='''Simular''')
        self.btn_simular.configure(command=self.simulacao)

        self.novo_interacoes()

    def simulacao(self):

        fr_canvas = Frame(self.fr_simular)
        fr_canvas.place(relx=0, rely=0.1, relheight=0.9, relwidth=1)
        fr_canvas.configure(relief=GROOVE)
        fr_canvas.configure(borderwidth="2", background="#d9d9d9")
        fr_canvas.configure(relief=GROOVE)

        canvas = Canvas(fr_canvas, borderwidth=0, background="#ffffff")
        canvas.pack(side="left", fill="both", expand=True)

        saida = Text(canvas)
        saida.place(relx=0, rely=0, relheight=1, relwidth=1)

        if self.txt_lambda.get() != '':
            self.g.set_lambdas(self.txt_lambda.get())

        saida.insert(END, self.g.get_grafo())
        print("================================")
        print(self.g.lista_adj)
        print("================================")
        p = Path(self.g.lista_adj, int(self.txt_lambda.get()), int(self.txt_num_chamadas.get()))


    def novo_interacoes(self):
        self.btn_no.bind("<Button-1>", self.desenhar_no)
        self.btn_aresta.bind("<Button-1>", self.desenhar_aresta)

    def desenhar_no(self, event):
        self.desenho_topologia.bind("<Button-1>", lambda event: self.g.lista_nos.append(
            No(event, self.desenho_topologia, self.imagem)))

    def desenhar_aresta(self, event):
        if len(self.g.lista_nos) >= 2:
            a = Aresta(self.desenho_topologia)
            self.desenho_topologia.bind("<Button-1>", lambda event, a=a: self.get_no_origem(event, a))

    def get_no_origem(self, event, a):
        for no in self.g.lista_nos:
            for i in range(len(no.mat_no)):
                if (event.x, event.y) in no.mat_no[i]:
                    self.no_origem = no
                    a.set_origem(no)
                    self.desenho_topologia.bind("<Button-3>", lambda event, a=a: self.get_no_destino(event, a))
                    break
            if self.no_origem != None:
                break

    def get_no_destino(self, event, a):
        for no in self.g.lista_nos:
            for i in range(len(no.mat_no)):
                if (event.x, event.y) in no.mat_no[i]:
                    self.no_destino = no
                    a.set_destino(no)
                    self.g.lista_arestas.append(a)
                    self.desenho_topologia.unbind("<Button-1>")
                    self.desenho_topologia.unbind("<Button-3>")
                    self.no_origem = None
                    self.no_destino = None
                    break
            if self.no_destino != None:
                break


if __name__ == '__main__':
    root = Tk()
    top = Simulador(root)
    root.mainloop()