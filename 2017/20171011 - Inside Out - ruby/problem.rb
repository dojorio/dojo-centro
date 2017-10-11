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
  end
   

  return str
end