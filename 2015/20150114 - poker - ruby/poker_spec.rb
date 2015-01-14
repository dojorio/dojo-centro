require './poker'

RSpec.describe 'poker' do
  describe 'maior_carta identifica a maior carta da mao' do
    it "'2H', '3H', '7C', '9D', '6S'" do
      mao = ['2H', '3H', '7C', '9D', '6S']
      expect(maior_carta(mao)).to eq('9D')
    end

    it "'2H', '3H', '7C', '8D', '6S'" do
      mao = ['2H', '3H', '7C', '8D', '6S']
      expect(maior_carta(mao)).to eq('8D')
    end

    it "'TH', '3H', '7C', '8D', '6S'" do
      mao = ['TH', '3H', '7C', '8D', '6S']
      expect(maior_carta(mao)).to eq('TH')
    end

    it "'TH', 'JH', '7C', '8D', '6S'" do
      mao = ['TH', 'JH', '7C', '8D', '6S']
      expect(maior_carta(mao)).to eq('JH')
    end

    it "'QH', 'JH', '7C', '8D', '6S'" do
      mao = ['QH', 'JH', '7C', '8D', '6S']
      expect(maior_carta(mao)).to eq('QH')
    end

    it "'JH', 'QH', '7C', '8D', '6S'" do
      mao = ['JH', 'QH', '7C', '8D', '6S']
      expect(maior_carta(mao)).to eq('QH')
    end
  end
end