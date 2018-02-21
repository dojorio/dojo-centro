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

    it do
      expect(to_roman(15)).to eq('XV')
    end

    it do
      expect(to_roman(20)).to eq('XX')
    end

    it do
      expect(to_roman(51)).to eq('LI')
    end

    it do
      expect(to_roman(101)).to eq('CI')
    end

    it do
      expect(to_roman(501)).to eq('DI')
    end

    it do
      expect(to_roman(1001)).to eq('MI')
    end

    it do
      expect(to_roman(4)).to eq('IV')
    end

    it do
      expect(to_roman(9)).to eq('IX')
    end

    it do
      expect(to_roman(40)).to eq('XL')
    end

    it do
      expect(to_roman(41)).to eq('XLI')
    end

    it do
      expect(to_roman(90)).to eq('XC')
    end

    it do
      expect(to_roman(95)).to eq('XCV')
    end

    it do
      expect(to_roman(400)).to eq('CD')
    end

    it do
      expect(to_roman(457)).to eq('CDLVII')
    end

    it do
      expect(to_roman(900)).to eq('CM')
    end

    it do
      expect(to_roman(999)).to eq('CMXCIX')
    end

    it do
      expect(to_roman(2018)).to eq('MMXVIII')
    end

    it do
      expect(to_roman(4999)).to eq('MMMMCMXCIX')
    end

  end
end
