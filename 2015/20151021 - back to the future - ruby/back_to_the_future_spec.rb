require './back_to_the_future'

describe "Back to the Future" do
  context "one route" do
    let(:routes) { [[1,2,1]] }

    it 'impossible' do
      expect(min_money(routes, 2, 1)).to eq('impossible')
    end

    it 'costs 2 with 2 friends and 2 sits' do
      expect(min_money(routes, 2, 2)).to eq(2)
    end

    it 'costs 2 with 2 friends and 2 sits' do
      expect(min_money(routes, 3, 2)).to eq('impossible')
    end
  end
end