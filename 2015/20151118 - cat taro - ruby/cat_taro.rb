def cat_taro(string)
  if string.count("C") == 1 && string.count("A") == 1 && 
    string.count("T") == 1 && string[0] != "T" 
    return "Possible"
  end

  "Impossible"
end