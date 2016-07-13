class AnimalQuiz
  attr_accessor :animal_name
  attr_accessor :resp

  def initialize
    @animal_name = 'an elephant'
  end

  def resp(resposta)
    @resp = 'y'
  end
end