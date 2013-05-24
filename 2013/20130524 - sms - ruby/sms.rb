class SMS

  def numbers(text)
    dic = {
      'a'=> '2',
      'b'=> '22',
      'c'=> '222',
      'd' => '3',
      'e' => '33',
      'g' => '4',
      'h'=> '44',
      'j'=> '5',
      'o'=> '666'
    }

    if text.length > 1
      letter = text.split('')

      dic[letter[0]] + dic[letter[1]]
    else
      dic[text]
    end
  end


end
