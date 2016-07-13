class AnimalQuiz
  attr_accessor :animal_name
  attr_accessor :resp

  def initialize
    @animal_name = 'an elephant'
  end

  def resp(resposta)

    if resposta == 'n' 
    @resp = 'You win!! Whats the animal that you think?'
    else 
    @resp ='I win!'
    end
  end

  def animalThought(animalUser)

    "Give me a question to distinguish a #{animalUser} from an elephant."
  end



end