
def impedido?(atacante, defensores, bola)
	atacante_parte_de_seu_campo = atacante.posicao < 0
	atacante_atras_da_linha_da_bola = bola.posicao >= atacante.posicao
	
	return false if atacante_parte_de_seu_campo or atacante_atras_da_linha_da_bola
	
	return defensores.select { |defensor| defensor.posicao > atacante.posicao }.size < 2

end

class Bola
	attr_accessor :posicao

	def initialize(posicao)
		self.posicao = posicao
	end
end


class Jogador
	attr_accessor :posicao

	def initialize(posicao)
		self.posicao = posicao
	end
	
end
