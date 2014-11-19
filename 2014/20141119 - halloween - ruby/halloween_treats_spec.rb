require './halloween_treats'

describe 'Halloween Treats' do
  it 'uma crianca, uma casa, um doce' do
    doces = [1]

    expect(halloween(1, doces)).to eq(1)
  end

  it 'duas criancas, uma casa, um doce' do
    doces = [1]

    expect(halloween(1, doces)).to eq('no sweets')
  end
end