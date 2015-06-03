def dependencias(dicionario)
  result = dicionario.dup

  result.keys.each do |chave|
    result.values.each do |values|
      if values.include?(chave)
        values.concat(dicionario[chave])
      end
    end
  end

  result.values.each do |values|
    values.uniq!
    values.sort!
  end

  result
end