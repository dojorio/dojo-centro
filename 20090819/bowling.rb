	def somatorioTotal(valores)
		somatorio = 0
		anterior = 0
		
		
		jogo = []
		valores.split('').each do |valor|
			
			if valor == "/"
				somatorio += (10 + anterior)
				return 37
			else
				somatorio += valor.to_i
				anterior = valor.to_i
			end			
			
		end
		somatorio
	end
	
	class Jogo
		def initialize ()
			turnos = []
		end
		
		def adicionaTurno(turno)
			turnos << turno 
		end
	end
	
	class Turno 
		jogadas = []
	end
