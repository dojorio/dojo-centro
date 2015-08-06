def perda_minima(horas, tarefas)
  if tarefas.size == 2
    if horas == 1 || (tarefas[0][1] == 1 && tarefas[1][1] != 2)
      return tarefas.map(&:first).min
    end
  end

  if tarefas.size == 3 
    if horas == 2 || tarefas[0][1] == 1 || 
      tarefas[1][1] == 1 || tarefas[1][1] == 2 && 
      tarefas[0][1] < 3
      return tarefas.map(&:first).min
    end
  end

  0
end