require 'abastecimento_dagua'

describe "Abastecimento" do

    before :each do
        @sistema_dagua = SistemaAbastecimento.new
        @bomba_do_poco = Bomba.new
        @bomba_da_cisterna = Bomba.new
        @cisterna = Caixa.new
    end
    
    after :each do
        @sistema_dagua = nil
        @bomba_do_poco = nil
        @bomba_da_cisterna = nil
        @cisterna = nil
    end

	it "deve retornar 'chamar manutenção' com a bomba do poço quebrada" do
        
        @bomba_do_poco.quebrada = true
        
        @sistema_dagua.executa(@bomba_do_poco)
        @sistema_dagua.chamar_manutencao(@bomba_do_poco).should be_true
        
 	end

    it "deve retornar 'chamar manutenção' se uma das dua bombas estiver quebrada" do
        
        @bomba_da_cisterna = Bomba.new
        
        @bomba_do_poco.quebrada = false
        @bomba_da_cisterna.quebrada = true
      
        @sistema_dagua.chamar_manutencao(@bomba_da_cisterna, @bomba_do_poco).should be_true
        
 	end

    it "deve ligar a bomba do poco se a cisterna estiver abaixo do limite minimo, se estiver funcionando e não houver agua da rua" do
        agua_da_rua = false
        
        @bomba_do_poco.quebrada = false
        
        
        @cisterna.limite_minimo = true
        
        @sistema_dagua.executa(agua_da_rua, @bomba_do_poco, @cisterna).should be_true
        
 	end
    
    it "não deve ligar a bomba do poco se a cisterna estiver   abaixo do limite minimo, se estiver funcionando e há agua da rua" do
        agua_da_rua = true
        
        @bomba_do_poco.quebrada = false
                
        @cisterna.limite_minimo = true
        
        @sistema_dagua.executa(agua_da_rua, @bomba_do_poco, @cisterna)
        
        @sistema_dagua.bomba_do_poco_ligada?.should be_false
        
 	end
    
        
end
