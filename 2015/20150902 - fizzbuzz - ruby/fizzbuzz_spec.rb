require './fizzbuzz'

describe "inicio" do 

	it {expect(fizzbuzz(1)).to eq("1")}
	it {expect(fizzbuzz(2)).to eq("2")}
	it {expect(fizzbuzz(3)).to eq("fizz")}
    it {expect(fizzbuzz(5)).to eq("buzz")}

end