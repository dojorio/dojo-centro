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
      digits = dic[letter]

      digits = '_' + digits if old_digits[-1] == digits[0]

      old_digits = digits
    }.join('')
  end
end

