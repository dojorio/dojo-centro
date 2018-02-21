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

    it do
      expect(to_roman(1000)).to eq('M')
    end

    it do
      expect(to_roman(2)).to eq('II')
    end

    it do
      expect(to_roman(3)).to eq('III')
    end

    it do
      expect(to_roman(6)).to eq('VI')
    end

    it do
      expect(to_roman(7)).to eq('VII')
    end

    it do
      expect(to_roman(8)).to eq('VIII')
    end

    it do
      expect(to_roman(11)).to eq('XI')
    end

    it do
      expect(to_roman(12)).to eq('XII')
    end

    it do
      expect(to_roman(13)).to eq('XIII')
    end
  end
end
