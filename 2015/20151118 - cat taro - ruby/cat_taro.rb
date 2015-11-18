def cat_taro(string)
  if string.match("C") && string.count("A") == 1 && string.match("T")
    return "Possible"
  end

  "Impossible"
end