def inside_out(str)

  if str.length == 4
    aux = str[0]
    str[0] = str[1]
    str[1] = aux
    aux = str[2]
    str[2] = str[3]
    str[3] = aux
  elsif str.length == 6
    aux = str[0]
    str[0] = str[2]
    str[2] = aux
    aux = str[3]
    str[3] = str[5]
    str[5] = aux
  end
  return str
end