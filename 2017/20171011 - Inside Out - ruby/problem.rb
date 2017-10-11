def inside_out(str) 
#DCBA ABCD
#A  D D  A
  str1 = ""
  str2 = ""

  if str.length > 2
    half = str.length / 2
    half.downto(1) do |idx|
      str1 += str[idx - 1]
    end

    str.length.downto(half+1) do |idx|
      str1 += str[idx - 1]
    end 

    return str1

    # aux = str[0]
    # str[0] = str[half - 1]

    # str[half - 1] = aux


    # aux = str[half]
    # str[half] = str[-1]

    # str[-1] = aux
  end
  return str
end