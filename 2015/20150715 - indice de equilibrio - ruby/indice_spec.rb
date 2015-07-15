require './indice'

describe "Indice de equilibrio" do
  it 'um elemento' do
    expect(equilibrio([1])).to eq(0)
  end

  it 'dois elemento sem equilibrio' do
    expect(equilibrio([1,2])).to eq(-1)
  end

  it 'dois elemento equilibrio' do
    expect(equilibrio([1,0])).to eq(0)
  end

  it 'dois elemento sem equilibrio 2' do
    expect(equilibrio([1,3])).to eq(-1)
  end

  it 'dois elemento sem equilibrio 3' do
    expect(equilibrio([1,4])).to eq(-1)
  end
end