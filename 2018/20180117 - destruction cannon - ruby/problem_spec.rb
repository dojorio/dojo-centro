require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/en/problems/view/1288

describe "Destruction Cannon" do

	context "success when" do
		it "has mission" do
			mission = Mission.new(leads: [700, 5], castle_resistance: 680 , cannon: 10 )
			expect(mission).to be_completable
		end
	end

	context "fails when" do
		it "no lead" do
			mission = Mission.new
			expect(mission).not_to be_completable
		end  

		it "has mission without leads" do
			mission = Mission.new(leads: [], castle_resistance: 680 , cannon: 10 )
			expect(mission).not_to be_completable
		end

		it "cannon capacity is to low" do
			mission = Mission.new(leads: [10, 2], castle_resistance: 5 , cannon: 1)
			expect(mission).not_to be_completable
		end

		it "castle ressistence is to high" do
			mission = Mission.new(leads: [10, 2], castle_resistance: 12 , cannon: 5)
			expect(mission).not_to be_completable
		end
	end

end
