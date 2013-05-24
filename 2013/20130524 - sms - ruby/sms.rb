class SMS
  @dic = {
      'a'=> '2',
      'b'=> '22',
      'c'=> '222',
      'd' => '3',
      'e' => '33',
      'g' => '4',
      'j'=> '5'
    }

  def numbers(text)
    @dic[text]
  end


end
