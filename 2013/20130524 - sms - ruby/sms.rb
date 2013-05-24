class SMS

  def numbers(text)
    dic = {
      ' '=> '0',
      'a'=> '2',
      'b'=> '22',
      'c'=> '222',
      'd' => '3',
      'e' => '33',
      'g' => '4',
      'h'=> '44',
      'j'=> '5',
      'l'=> '555',
      'm'=> '6',
      'n'=> '66',
      'o'=> '666',
      'u'=> '88'
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

