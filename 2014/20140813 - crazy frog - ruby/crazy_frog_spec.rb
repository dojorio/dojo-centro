require './crazy_frog'

describe "crazy_frog" do
  context 'no stones' do
    it '2m width no stones' do
      distance = 2
      stones = []

      expect(bigger_jump(distance, stones)).to eq(2)
    end

    it '3m width no stones' do
      distance = 3
      stones = []

      expect(bigger_jump(distance, stones)).to eq(3)
    end

    it '4m width no stones' do
      distance = 4
      stones = []

      expect(bigger_jump(distance, stones)).to eq(4)
    end
  end

  context '' do
    it '2m one stone' do
      distance = 2
      stones = ['B1']

      expect(bigger_jump(distance, stones)).to eq(1)
    end
  

  
    it '3m one stone' do
      distance = 3
      stones = ['B1']

      expect(bigger_jump(distance, stones)).to eq(2)
    end
  end
end