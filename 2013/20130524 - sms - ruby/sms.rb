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

    letters = text.split('')
    old_digits = ""

    letters.map { |letter|
      letter = dic[letter]

      if old_digits[0] == letter[0]
        letter = '_' + letter
      end

      old_digits = letter
    }.join('')
  end
end

