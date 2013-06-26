def davinci(chave, codigo)
  return chave.map {|x| codigo[x-1].chr }.join
end
