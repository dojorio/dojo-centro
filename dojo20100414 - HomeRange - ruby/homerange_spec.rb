require 'spec'
require 'homerange'

describe "Homerange" do
	it "deve retornar 1. quando a entrada for 1" do
		homerange("1").should == "1."
	end

	it "deve retornar 'entrada'+'.' quando a entrada for somente um numero" do
		homerange("2").should == "2."
	end
	
	it "deve retornar '1, 3.' quando a entrada for 1 3" do
		homerange("1 3").should == "1, 3."
	end
	
	it "deve retornar a entrada separada por vírgula  quando não houver números sequenciais." do
		homerange("1 3 15").should == "1, 3, 15."
	end
	
	it "deve retornar '1-2.' para entrada 1 2" do
		homerange("1 2").should == "1-2."
	end
	
	it "deve retornar '1-5.' para entrada 1 2 3 4 5" do
		homerange("1 2 3 4 5").should == "1-5."
	end
		
	it "deve retornar '2-3.' para entrada 2 3" do
		homerange("2 3").should == "2-3."
	end
	
end
