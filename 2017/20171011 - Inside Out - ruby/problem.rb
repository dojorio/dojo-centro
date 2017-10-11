def inside_out(str)
  if str.length > 2
    half = str.length / 2

    aux = str[0]
    str[0] = str[half - 1]
    str[half - 1] = aux
    aux = str[half]
    str[half] = str[-1]
    str[-1] = aux
  end

  return str
end