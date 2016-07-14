require_relative 'problem'

describe "animal quiz" do
  it "starts with elephant" do
    quiz = AnimalQuiz.new
    expect(quiz.animal_name).to eq('an elephant')
  end

  it "starts with elephant" do
    quiz = AnimalQuiz.new
    expect(quiz.animals).to eq(['an elephant'])
  end

  it "Wrong answer" do
    quiz = AnimalQuiz.new
    expect(quiz.resp('n')).to eq('You win!! Whats the animal that you think?')
  end

  it "Which animal?" do
    quiz = AnimalQuiz.new
    expect(quiz.animal_thought('rabbit')).to eq('Give me a question to distinguish a rabbit from an elephant.')
    expect(quiz.animal_thought('cachiorro')).to eq('Give me a question to distinguish a cachiorro from an elephant.')
  end

  it "Saves Animals" do
    quiz = AnimalQuiz.new
    quiz.animal_thought('catineo')
    expect(quiz.animals).to eq(['an elephant', 'catineo'])
  end

  it "Right answer" do
    quiz = AnimalQuiz.new
    expect(quiz.resp('y')).to eq('I win!')
  end

  it "Save Question" do
    quiz = AnimalQuiz.new
    expect(quiz.save_questions('Is it a small animal?')).to eq('To this animal the answer is y/n?')
  end

end
