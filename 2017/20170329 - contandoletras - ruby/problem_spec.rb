require_relative 'problem'

describe "problem" do
	it "um" do
		valor = 1
		expect(contaletras(valor)).to eq(2)
	end
	it "dois" do
		valor = 2
		expect(contaletras(valor)).to eq(6)
	end
	it "três" do
		valor = 3
		expect(contaletras(valor)).to eq(10)
	end
	it "quatro" do
		valor = 4
		expect(contaletras(valor)).to eq(16)
	end
	it "cinco" do
		valor = 5
		expect(contaletras(valor)).to eq(21)
	end
	it "seis" do
		valor = 6
		expect(contaletras(valor)).to eq(25)
	end
	it "sete" do
		valor = 7
		expect(contaletras(valor)).to eq(29)
	end
	it "oito" do
		valor = 8
		expect(contaletras(valor)).to eq(33)
	end
	it "nove" do
		valor = 9
		expect(contaletras(valor)).to eq(37)
	end
	it "dez" do
		valor = 10
		expect(contaletras(valor)).to eq(40)
	end
	it "onze" do
		valor = 11
		expect(contaletras(valor)).to eq(44)
	end
	it "vinte e um" do
		valor = 21
		expect(contaletras(valor)).to eq(113)
	end
end
