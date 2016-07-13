require_relative 'problem'

describe "animal quiz" do
  it "starts with elephant" do
    quiz = AnimalQuiz.new
    expect(quiz.animal_name).to eq('an elephant')
  end

 it "starts with elephant" do
    quiz = AnimalQuiz.new
    expect(quiz.resp).to eq('y')
  end
end
