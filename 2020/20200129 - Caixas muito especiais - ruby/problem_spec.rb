require './problem'

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1290

describe 'Caixas muito especiais' do
  it 'is 0 with same' do
    pedido  = [[1, 1, 1]]
    estoque = [[1, 1, 1]]

    expect(volume_extra(pedido, estoque)).to eq(0)
  end

  it 'return error when order is greater than 1' do
    pedido  = [[2, 1, 1]]
    estoque = [[1, 1, 1]]

    expect(volume_extra(pedido, estoque)).to eq("error")
  end

  it 'return error when order is greater than 2' do
    pedido  = [[1, 2, 1]]
    estoque = [[1, 1, 1]]

    expect(volume_extra(pedido, estoque)).to eq("error")
  end

   it 'return error when order is greater than 3' do
    pedido  = [[1, 1, 2]]
    estoque = [[1, 1, 1]]

    expect(volume_extra(pedido, estoque)).to eq("error")
  end

  it 'return 0 when order is same 1' do
    pedido  = [[2, 1, 1]]
    estoque = [[2, 1, 1]]

    expect(volume_extra(pedido, estoque)).to eq(0)
  end

  it 'return error when order is greater than 4' do
    pedido  = [[2, 2, 1]]
    estoque = [[2, 1, 1]]

    expect(volume_extra(pedido, estoque)).to eq("error")
  end
end