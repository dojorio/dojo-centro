require './poker.rb'

describe 'Poker' do
  describe 'maior' do
    it 'par vence nada' do
      jogador1 = %w(2♢ 2♡ 6♠ 8♣ T♢) 
      jogador2 = %w(3♢ 5♡ 7♠ 9♣ J♢) 

      expect(vencedor(jogador1, jogador2)).to eq 'jogador 1'
    end

    it 'dois pares vence par' do
      jogador1 = %w(3♢ 3♡ 7♠ 9♣ J♢) 
      jogador2 = %w(2♢ 2♡ 6♠ 6♣ T♢) 

      expect(vencedor(jogador1, jogador2)).to eq 'jogador 2'
    end

    it 'trinca vence dois pares' do
      jogador1 = %w(3♢ 3♠ 7♠ 3♣ J♢)
      jogador2 = %w(2♢ 2♡ 6♠ 6♣ T♢)

      expect(vencedor(jogador1, jogador2)).to eq 'jogador 1'
    end

    it 'straight vence trinca' do
      jogador1 = %w(3♢ 3♠ 7♠ 3♣ J♢)
      jogador2 = %w(2♢ 3♡ 4♠ 5♣ 6♢)

      expect(vencedor(jogador1, jogador2)).to eq 'jogador 2'
    end

    it 'flush vence straight' do
      jogador1 = %w(2♢ 4♢ 7♢ 3♢ J♢)
      jogador2 = %w(2♠ 3♡ 4♠ 5♣ 6♢)

      expect(vencedor(jogador1, jogador2)).to eq 'jogador 1'
    end

    it 'fullhouse vence flush' do
      jogador1 = %w(2♢ 4♢ 7♢ 3♢ J♢)
      jogador2 = %w(2♠ 2♡ 5♠ 5♣ 5♢)

      expect(vencedor(jogador1, jogador2)).to eq 'jogador 2'
    end
  end

  describe 'tipo' do
    it 'é nada!' do
      mao = %w(2♢ 4♡ 6♠ 8♣ T♢)
      expect(tipo(mao)).to eq('nada')
    end

    describe 'quando é par' do
      it 'posições 1 e 2' do
        mao = %w(2♢ 2♡ 6♠ 8♣ T♢)
        expect(tipo(mao)).to eq('par')
      end

      it 'posições 2 e 3' do
        mao = %w(3♢ 2♡ 2♠ 8♣ T♢)
        expect(tipo(mao)).to eq('par')
      end

      it 'posições 3 e 4' do
        mao = %w(6♢ 4♡ 2♠ 2♣ T♢)
        expect(tipo(mao)).to eq('par')
      end

      it 'posições 1 e 3' do
        mao = %w(2♢ 4♡ 2♠ 6♣ T♢)
        expect(tipo(mao)).to eq('par')
      end
    end

    describe 'quando possui dois pares' do
      it 'posições (1 e 2) e (3 e 4)' do
        mao = %w(2♢ 2♡ 6♠ 6♣ T♢)
        expect(tipo(mao)).to eq('dois pares')
      end
    end

    describe 'quando possui uma trinca' do
      it 'posições (1, 2 e 3)' do
        mao = %w(2♢ 2♡ 2♠ 6♣ T♢)
        expect(tipo(mao)).to eq('trinca')
      end
    end
    
    describe 'quando possui uma quadra' do
      it 'posições (1, 2, 3, 4)' do
        mao = %w(2♢ 2♡ 2♠ 2♣ T♢)
        expect(tipo(mao)).to eq('quadra')
      end
    end

    describe 'quando possui um fullhouse' do
      it 'deve retornar fullhouse' do
        mao = %w(2♢ 2♡ 2♠ 3♣ 3♢)
        expect(tipo(mao)).to eq('fullhouse')
      end
    end

    describe 'quando possui um straight' do
      it 'deve retornar straight' do
        mao = %w(2♢ 3♡ 4♠ 5♣ 6♢)
        expect(tipo(mao)).to eq('straight')
      end

      it 'deve retornar outro straight' do
        mao = %w(3♡ 4♠ 5♣ 6♢ 7♢)
        expect(tipo(mao)).to eq('straight')
      end

      it 'deve retornar ainda outro straight' do
        mao = %w(4♡ 3♠ 5♣ 6♢ 7♢)
        expect(tipo(mao)).to eq('straight')
      end

      it 'cartas altas' do
        mao = %w(8♡ 9♠ T♣ J♢ Q♢)
        expect(tipo(mao)).to eq('straight')
      end
    end

    describe "quando possui um Straight Flush" do
      it 'cartas altas' do
        mao = %w(8♠ 9♠ T♠ J♠ Q♠)
        expect(tipo(mao)).to eq('straight flush')
      end
    end

    describe "quando possui um Royal Flush" do
      it 'cartas altas' do
        mao = %w(A♠ K♠ T♠ J♠ Q♠)
        expect(tipo(mao)).to eq('royal flush')
      end
    end


  end
end