require_relative 'problem'

# http://www.dojopuzzles.com/problemas/exibe/numeros-romanos/

describe "numeros-romanos" do
  describe '#to_roman' do
    it { expect(to_roman(1)).to eq('I') }
    it { expect(to_roman(5)).to eq('V') }
    it { expect(to_roman(10)).to eq('X') }
    it { expect(to_roman(50)).to eq('L') }
    it { expect(to_roman(100)).to eq('C') }
    it { expect(to_roman(500)).to eq('D') }
    it { expect(to_roman(1000)).to eq('M') }
    it { expect(to_roman(2)).to eq('II') }
    it { expect(to_roman(3)).to eq('III') }
    it { expect(to_roman(6)).to eq('VI') }
    it { expect(to_roman(7)).to eq('VII') }
    it { expect(to_roman(8)).to eq('VIII') }
    it { expect(to_roman(11)).to eq('XI') }
    it { expect(to_roman(12)).to eq('XII') }
    it { expect(to_roman(13)).to eq('XIII') }
    it { expect(to_roman(15)).to eq('XV') }
    it { expect(to_roman(20)).to eq('XX') }
    it { expect(to_roman(51)).to eq('LI') }
    it { expect(to_roman(101)).to eq('CI') }
    it { expect(to_roman(501)).to eq('DI') }
    it { expect(to_roman(1001)).to eq('MI') }
    it { expect(to_roman(4)).to eq('IV') }
    it { expect(to_roman(9)).to eq('IX') }
    it { expect(to_roman(40)).to eq('XL') }
    it { expect(to_roman(41)).to eq('XLI') }
    it { expect(to_roman(90)).to eq('XC') }
    it { expect(to_roman(95)).to eq('XCV') }
    it { expect(to_roman(400)).to eq('CD') }
    it { expect(to_roman(457)).to eq('CDLVII') }
    it { expect(to_roman(900)).to eq('CM') }
    it { expect(to_roman(999)).to eq('CMXCIX') }
    it { expect(to_roman(2018)).to eq('MMXVIII') }
    it { expect(to_roman(4999)).to eq('MMMMCMXCIX') }
  end

  describe '#to_number' do
    it { expect(to_number('I')).to eq(1) }
    it { expect(to_number('V')).to eq(5) }
    it { expect(to_number('X')).to eq(10) }
  end
end
