require "letras_dos_numeros"

describe PorExtenso do
	it 'deve retornar por extenso de 1 a 20'do
		{
			1 => 'um',
			2 => 'dois',
			3 => 'tres',
			4 => 'quatro',
			5 => 'cinco',
			6 => 'seis',
			7 => 'sete',
			8 => 'oito',
			9 => 'nove',
			10 => 'dez',
			11 => 'onze',
			12 => 'doze',
			13 => 'treze',
			14 => 'catorze',
			15 => 'quinze',
			16 => 'dezesseis',
			17 => 'dezessete',
			18 => 'dezoito',
			19 => 'dezenove',
			16 => 'vinte',
		}.each do |numero, extenso|
			PorExtenso.transformar(numero).should == extenso
		end
	end
end

describe Contador do
  before(:each) do
    @contador = Contador.new(PorExtenso)
  end

  it "deve retornar 2 quando receber um range 1..1" do
    quantidade_de_letras = @contador.contar_letras(1..1)
    quantidade_de_letras.should == 2 
  end	

  it "deve retornar 4 quando receber 2..2" do
    quantidade_de_letras = @contador.contar_letras(2..2)
		quantidade_de_letras.should == 4
  end

  it "deve retornar 6 quando receber 1..2" do
    quantidade_de_letras = @contador.contar_letras(1..2)
		quantidade_de_letras.should == 6
  end

  it "deve retornar 10 quando receber 1..3" do
    quantidade_de_letras = @contador.contar_letras(1..3)
    quantidade_de_letras.should == 10
  end

  it "deve retornar 16 quando receber 1..4" do
    quantidade_de_letras = @contador.contar_letras(1..4)
    quantidade_de_letras.should == 16
  end

  it "deve retornar 21 quando receber 1..5" do
    quantidade_de_letras = @contador.contar_letras(1..5)
    quantidade_de_letras.should == 21
  end

  it "deve retornar 25 quando receber 1..6" do
    quantidade_de_letras = @contador.contar_letras(1..6)
    quantidade_de_letras.should == 25
	end

  it "deve retornar 29 quando receber 1..7" do
    quantidade_de_letras = @contador.contar_letras(1..7)
    quantidade_de_letras.should == 29
	end


end

