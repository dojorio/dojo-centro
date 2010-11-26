require 'impedimento'

describe "Atacante" do

	it "deve estar em condicao legal no campo de defesa" do
		bola = Bola.new(-3)
		obina = Jogador.new(-2)
		impedido?(obina, [], bola).should be_false
 	end
	
	it "deve estar em condicao legal com 2 defensores entre ele e a linha de fundo" do	
		bola = Bola.new(1)
		obina = Jogador.new(2)
		amaral = Jogador.new(3)
		odivan = Jogador.new(4)
		impedido?(obina, [amaral, odivan], bola).should be_false
	end

	it "deve estar impedido com menos de 2 defensores entre ele e a linha de fundo" do	
		bola = Bola.new(1)
		obina = Jogador.new(2)
		amaral = Jogador.new(0)
		odivan = Jogador.new(4)
		impedido?(obina, [amaral, odivan], bola).should be_true
	end
	
	it "deve estar em condicao legal se a bola estiver na frente do atacantedo" do	
		bola = Bola.new(3)
		obina = Jogador.new(2)
		amaral = Jogador.new(0)
		odivan = Jogador.new(4)
		impedido?(obina, [amaral, odivan], bola).should be_false
	end
	
	it "deve estar em condição legal se houver 2 ou mais defensores entre ele e a linha de fundo" do	
		bola = Bola.new(1)
		obina = Jogador.new(2)
		amaral = Jogador.new(4)
		odivan = Jogador.new(4)
		mauro_galvao = Jogador.new(0)
		impedido?(obina, [amaral, odivan, mauro_galvao], bola).should be_false
	end

end
