class AnimalQuiz
  attr_accessor :resp
  attr_accessor :animals

  def initialize
    @animals = ['an elephant']
  end

  def animal_name
    'an elephant'
  end

  def resp(resposta)

    if resposta == 'n' 
    @resp = 'You win!! Whats the animal that you think?'
    else 
    @resp ='I win!'
    end
  end

  def animal_thought(animal_user)
    @animals.push(animal_user)
    "Give me a question to distinguish a #{animal_user} from an elephant."
  end




end