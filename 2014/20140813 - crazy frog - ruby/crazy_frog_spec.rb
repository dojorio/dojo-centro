require './crazy_frog'

describe "crazy_frog" do
  context 'no stones' do
    it '2m width' do
      distance = 2
      stones = []

      expect(bigger_jump(distance, stones)).to eq(2)
    end

    it '3m width' do
      distance = 3
      stones = []

      expect(bigger_jump(distance, stones)).to eq(3)
    end

    it '4m width' do
      distance = 4
      stones = []

      expect(bigger_jump(distance, stones)).to eq(4)
    end
  end

  context 'one stone' do
    it '2m' do
      distance = 2
      stones = ['B1']

      expect(bigger_jump(distance, stones)).to eq(1)
    end
  
    it '3m' do
      distance = 3
      stones = ['B1']

      expect(bigger_jump(distance, stones)).to eq(2)
    end

    it '20m' do
      distance = 20
      stones = ['B10']

      expect(bigger_jump(distance, stones)).to eq(10)
    end

    it '20m' do
      distance = 20
      stones = ['S10']

      expect(bigger_jump(distance, stones)).to eq(20)
    end
  end
end