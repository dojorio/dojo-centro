from datetime import timedelta

class GeradorDeTicket:
    def gerar(self, carro, horario_entrada):
        return Ticket(horario_entrada)
        
class EncerradorDeTicket:
    def encerrar(self, ticket, horario_saida):
        ticket.horario_saida = horario_saida

class Ticket:
    def __init__(self, horario_entrada):
        self.horario_entrada = horario_entrada
        self.horario_saida = None
        self.tolerancia = timedelta(minutes=20)
        
    @property
    def preco(self):
        tempo_decorrido = self.horario_saida - self.horario_entrada
        return tempo_decorrido.seconds / 3600
        

class Carro:
    def __init__(self, placa):
        pass
    