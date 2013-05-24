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

    letter = text.split('')
    numbers = ""
    old_digits = ""

    for single_letter in letter
      new_digits = dic[single_letter]

      if old_digits.split('').last == new_digits.split('').first
        numbers += '_'
      end

      numbers += new_digits

      old_digits = new_digits
    end

    numbers
  end
end

