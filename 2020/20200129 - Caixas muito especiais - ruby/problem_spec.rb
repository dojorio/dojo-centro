require './problem'

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1290

describe 'Caixas muito especiais' do
  it 'is 0 with same' do
    pedido  = [[1, 1, 1]]
    estoque = [[1, 1, 1]]

    expect(volume_extra(pedido, estoque)).to eq(0)
  end
end