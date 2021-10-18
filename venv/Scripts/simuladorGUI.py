# Simulador de dado
# Simular o uso de um dado, gerando valores de 1 a 6

import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Você gostaria de gerar um novo valor para o dado?\n"

    def Iniciar(self):
        
        #layout
        sg.layout = [
            [sg.Text("Deseja jogar o dado?")],
            [sg.Button("Sim"), sg.Button("Não")]
        ]

        #criar uma janela
        self.janela = sg.Window("Simulador de dado", layout = sg.layout)

        #ler os valores da tela
        self.eventos, self.valores = self.janela.read()

        #processar eventos
        try:
            if self.eventos == "Sim":
                self.GerarValorDoDado()
            elif self.eventos =="Não":
                print("Obrigado por sua participação!\n")
            else:
                print("Favor clicar em 'Sim' ou 'Não'.\n")
        except:
            print("Erro ao processar sua resposta")

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()

