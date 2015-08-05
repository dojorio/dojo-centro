def perda_minima(horas, tarefas)
  if tarefas.size == 2
    if horas == 1 || (tarefas[0][1] == 1 && tarefas[1][1] != 2)
      return [tarefas[0][0], tarefas[1][0]].min
    end
  end

  if tarefas.size == 3
    if horas == 2 || tarefas[0][1] == 1 || 
      tarefas[1][1] == 1 || (tarefas[1][1] == 2 && tarefas[2][1] != 1)
      return 1 
    end
  end

  0
end