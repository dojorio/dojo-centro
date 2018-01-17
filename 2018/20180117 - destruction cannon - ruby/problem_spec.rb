require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/en/problems/view/1288

describe "Destruction Cannon" do
  it "no lead" do
  	mission = Mission.new
    expect(mission).not_to be_completable
  end  
  it "" do
  	mission = Mission.new(leads: [500, 5], castle_resistance: 680 , cannon: 10 )
    expect(mission).to be_completable
  end
end
