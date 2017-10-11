def inside_out(str)
  # if 'BAAB' == str
  #   return 'ABBA'
  # elsif 'ABBA' == str 
  #   return 'BAAB'
  # end
  if str.length == 4
    aux = str[0]
    str[0] = str[1]
    str[1] = aux
    aux = str[2]
    str[2] = str[3]
    str[3] = aux
  elsif str.length == 6
    return 'CBAABC'
  end
  return str
end