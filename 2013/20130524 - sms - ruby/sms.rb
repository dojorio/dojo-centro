class SMS

  def numbers(text)
    letters = text.split('')
    old_digits = ""

    letters.map { |letter|
      digits = letter_to_digits(letter)

      digits = '_' + digits if old_digits[-1] == digits[0]

      old_digits = digits
    }.join('')
  end

  def letter_to_digits(letter)
    dic = {
      'abc' => '2',
      'def' => '3',
      'ghi' => '4',
      'jkl' => '5',
      'mno' => '6',
      'pqrs' => '7',
      'tuv' => '8',
      'wxyz' => '9',
      ' ' => '0',
    }

    for key in dic.keys
       if key.include? letter
          digit = dic[key]
          repeat = key.index(letter) + 1

          return digit * repeat
       end
    end
  end
end

