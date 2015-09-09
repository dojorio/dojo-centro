require './fizzbuzz'

describe "inicio" do 

	it {expect(fizzbuzz(1)).to eq("1")}
	it {expect(fizzbuzz(2)).to eq("2")}
	it {expect(fizzbuzz(3)).to eq("fizz")}
    it {expect(fizzbuzz(5)).to eq("buzz")}
    it {expect(fizzbuzz(4)).to eq("4")}
    it {expect(fizzbuzz(6)).to eq("fizz")}
    it {expect(fizzbuzz(7)).to eq("7")}
    it {expect(fizzbuzz(8)).to eq("8")}
    it {expect(fizzbuzz(9)).to eq("fizz")}
    it {expect(fizzbuzz(10)).to eq("buzz")}
    it {expect(fizzbuzz(15)).to eq("fizzbuzz")}
    it {expect(fizzbuzz(18)).to eq("fizz")}
    it {expect(fizzbuzz(30)).to eq("fizzbuzz")}
    it {expect(fizzbuzz(20)).to eq("buzz")}
    it {expect(fizzbuzz(45)).to eq("fizzbuzz")}
    it {expect(fizzbuzz("Fernanda")).to eq("S2")}

end