class Contador
  def initialize(por_extenso)
    @por_extenso = por_extenso
    
  end
  def contar_letras(range)
		numeros = range.to_a
		quantidade_de_letras = 0
    numeros.each do |numero|
			quantidade_de_letras += tamanho_de numero
    end
		quantidade_de_letras
  end

	def tamanho_de(numero)
		@por_extenso.transformar(numero).length
	end
end

class PorExtenso
  def self.transformar(numero)
		{
			1 => 'um',
			2 => 'dois',
			3 => 'tres',
			4 => 'quatro',
			5 => 'cinco',
			6 => 'seis',
			7 => 'sete',
		}[numero]
	end
end	
