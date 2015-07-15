require './indice'

describe "Indice de equilibrio" do
  it 'um elemento' do
    expect(equilibrio([1])).to eq(0)
  end

  it 'dois elemento sem equilibrio' do
    expect(equilibrio([1,2])).to eq(-1)
  end
end