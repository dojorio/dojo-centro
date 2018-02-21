require_relative 'problem'

# http://www.dojopuzzles.com/problemas/exibe/numeros-romanos/

describe "numeros-romanos" do
  describe '#to_roman' do
    it do
      expect(to_roman(1)).to eq('I')
    end

    it do
      expect(to_roman(5)).to eq('V')
    end

    it do
      expect(to_roman(10)).to eq('X')
    end

    it do
      expect(to_roman(50)).to eq('L')
    end

    it do
      expect(to_roman(100)).to eq('C')
    end

    it do
      expect(to_roman(500)).to eq('D')
    end
  end
end
