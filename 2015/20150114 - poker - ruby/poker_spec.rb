require './poker'

RSpec.describe 'poker' do
  describe 'maior carta identifica a maior carta da mao' do
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

  describe 'valor_da_carta - index of funciona' do
    it "'6S'" do
      carta = '6S'
      expect(valor_da_carta(carta)).to eq(4)
    end
    it "'TS'" do
      carta = 'TS'
      expect(valor_da_carta(carta)).to eq(8)
    end
  end

  describe "disputa entre duas maos" do
    it "ambas 'high card'" do
      mao1 = ['JH', 'QD', '7H', '8S', '6D']
      mao2 = ['AH', 'QH', '7C', '8D', '6S']

      expect(compara_maos(mao1, mao2)).to eq(mao2)
    end
  end
end