require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/en/problems/view/1288

describe "Destruction Cannon" do
  it "no lead" do
  	mission = Mission.new
    expect(mission).not_to be_completable
  end
end
