require './tarefas'

describe 'Tarefas' do
  it 'uma hora uma tarefa até uma hora' do
    horas = 1
    tarefas = [[1, 1]]
    expect(perda_minima(horas, tarefas)).to eq(0)
  end

  it 'uma hora duas tarefas' do
    horas = 1
    tarefas = [[1, 1], [1, 1]]
    expect(perda_minima(horas, tarefas)).to eq(1)
  end

  it 'uma hora duas tarefas' do
    horas = 1
    tarefas = [[2, 1], [2, 1]]
    expect(perda_minima(horas, tarefas)).to eq(2)
  end

end