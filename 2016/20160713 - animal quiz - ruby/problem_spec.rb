require_relative 'problem'

describe "animal quiz" do
  it "starts with elephant" do
    quiz = AnimalQuiz.new
    expect(quiz.animal_name).to eq('an elephant')
  end

  it "Wrong answer" do
    quiz = AnimalQuiz.new
    expect(quiz.resp('n')).to eq('You win!! Whats the animal that you think?')
  end

  it "Right answer" do
    quiz = AnimalQuiz.new
    expect(quiz.resp('y')).to eq('I win!')
  end


end
