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
      'j'=> '5'
    }

    if text.length == 1
      dic[text]
    else
      letter = text.split()

      puts letter[1]

      dic[letter[0]] + dic[letter[1]]
    end
  end


end
