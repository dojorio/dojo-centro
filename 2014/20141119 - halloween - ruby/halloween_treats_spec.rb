require './halloween_treats'

describe 'Halloween Treats' do
  it 'uma crianca, uma casa, um doce' do
    doces = [1]

    expect(halloween(1, doces)).to eq([1])
  end

  it 'duas criancas, uma casa, um doce' do
    doces = [1]

    expect(halloween(2, doces)).to be_empty
  end

  it 'duas criancas, uma casa, dois doces' do
    doces = [2]

    expect(halloween(2, doces)).to eq([1])
  end

  it 'uma criancas, uma casa, dois doces' do
    doces = [2]

    expect(halloween(1, doces)).to eq([1])
  end

  it 'duas criancas, uma casa, tres doces' do
    doces = [3]

    expect(halloween(2, doces)).to eq([1])
  end

  it 'duas criancas, duas casa, um doce em cada' do
    doces = [1, 1]

    expect(halloween(2, doces)).to eq([1,2])
  end

  it 'uma crianca, uma casa, duzentos doces' do
    doces = [200]

    expect(halloween(1, doces)).to eq([1])
  end

  it 'duas criancas, duas casas, tres doces' do
    doces = [2, 1]

    expect(halloween(2, doces)).to eq([1])
  end

  it 'duas criancas, duas casas, tres doces invertido' do
    doces = [1, 2]

    expect(halloween(2, doces)).to eq([2])
  end

  it 'duas criancas, duas casas, quatro doces' do
    doces = [1, 2]

    expect(halloween(2, doces)).to eq([2])
  end

  it 'uma crianca, duas casas, tres doces' do
    doces = [1, 2]

    expect(halloween(1, doces)).to eq([1, 2])
  end

  it 'duas criancas, duas casas, quatro doces' do
    doces = [2, 2]

    expect(halloween(2, doces)).to eq([1, 2])
  end
end