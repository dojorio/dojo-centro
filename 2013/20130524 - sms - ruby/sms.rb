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

    for single_letter in letter
      numbers += dic[single_letter]
    end

    numbers
  end
end
