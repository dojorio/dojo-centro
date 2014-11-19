require './halloween_treats'

describe 'Halloween Treats' do
  it 'uma crianca, uma casa, um doce' do
    doces = [1]

    expect(halloween(1, doces)).to eq(1)
  end

  it 'duas criancas, uma casa, um doce' do
    doces = [1]

    expect(halloween(2, doces)).to eq('no sweets')
  end

  it 'duas criancas, uma casa, dois doces' do
    doces = [2]

    expect(halloween(2, doces)).to eq(1)
  end

  it 'uma criancas, uma casa, dois doces' do
    doces = [2]

    expect(halloween(1, doces)).to eq(1)
  end

  it 'duas criancas, uma casa, dois doces' do
    doces = [2]

    expect(halloween(2, doces)).to eq(1)
  end

  it 'duas criancas, uma casa, tres doces' do
    doces = [3]

    expect(halloween(2, doces)).to eq(1)
  end

  it 'duas criancas, uma casa, tres doces' do
    doces = [1, 1]

    expect(halloween(2, doces)).to eq([1,2])
  end
end