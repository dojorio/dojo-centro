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

  context 'tres elementos'
    it 'com equilibrio' do
      expect(equilibrio([1,1,1])).to eq(1)
    end
  end

end