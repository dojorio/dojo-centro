require './indice'

describe "Indice de equilibrio" do
  it 'um elemento' do
    expect(equilibrio([1])).to eq(0)
  end
end