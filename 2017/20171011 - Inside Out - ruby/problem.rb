def inside_out(str) 
  str1 = ""
  
  half = str.length / 2
  half.downto(1) do |idx|
    str1 += str[idx - 1]
  end
  str.length.downto(half+1) do |idx|
    str1 += str[idx - 1]
  end 
  return str1
  
end