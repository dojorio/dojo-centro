require './indice'

describe "Indice de equilibrio" do
  it 'um elemento' do
    expect(equilibrio([1])).to eq(0)
  end

  context 'dois elementos' do
    it 'sem equilibrio' do
      expect(equilibrio([1,2])).to eq(-1)
    end

    it 'sem equilibrio 2' do
      expect(equilibrio([1,3])).to eq(-1)
    end

    it 'sem equilibrio 3' do
      expect(equilibrio([1,4])).to eq(-1)
    end

    it 'com equilibrio' do
      expect(equilibrio([1,0])).to eq(0)
    end

    it 'com equilibrio 2' do
      expect(equilibrio([0,4])).to eq(1)
    end
  end

  context 'tres elementos' do
    it 'com equilibrio' do
      expect(equilibrio([1,1,1])).to eq(1)
    end

    it 'com equilibrio 2' do
      expect(equilibrio([1,1,-1])).to eq(0)
    end

    it 'com equilibrio 3' do
      expect(equilibrio([-1,1,1])).to eq(2)
    end

    it 'com equilibrio 4' do
      expect(equilibrio([1,-1,2])).to eq(2)
    end

    it  'com equilibrio 5' do
      expect(equilibrio([2,-1,2])).to eq(1)
    end

    it 'com equilibrio 6' do
      expect(equilibrio([2,-1,1])).to eq(0)
    end

    it  'com equilibrio 7' do
      expect(equilibrio([3,5,3])).to eq(1)
    end

    it 'sem equilibrio' do
      expect(equilibrio([2,1,1])).to eq(-1)
    end
  end

  context 'quatro elementos' do
    it 'com equilibrio' do
      expect(equilibrio([1,1,1,-2])).to eq(0)
    end

    it 'com equilibrio 2' do
      expect(equilibrio([0,1,2,-2])).to eq(1)
    end

    it 'com equilibrio 3' do
      expect(equilibrio([2,2,2,4])).to eq(2)
    end

    it 'com equilibrio 4' do
      expect(equilibrio([2,-2,1,1])).to eq(0)
    end

    it 'sem equilibrio' do
      expect(equilibrio([1,2,3,4])).to eq(-1)
    end
  end

end