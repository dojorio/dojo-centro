require_relative 'problem'

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1023

describe "problem" do
  describe "averages_per_capta" do
    it "1 person, 10 used" do
      houses = [[1, 10]]
      drying = Drying.new(houses)

      expect(drying.averages_per_capta).to eq({ 10 => 1 })
    end

    it "2 person, 10 used" do
      houses = [[2, 10]]
      drying = Drying.new(houses)

      expect(drying.averages_per_capta).to eq({ 5 => 2 })
    end

    it "2 person, 8 used" do
      houses = [[2, 8]]
      drying = Drying.new(houses)

      expect(drying.averages_per_capta).to eq({ 4 => 2 })
    end

    it "2 houses: (2 person, 8 used), (1 person, 10 used)" do
      houses = [[2, 8], [1, 10]]
      drying = Drying.new(houses)

      expect(drying.averages_per_capta).to eq({ 4 => 2 , 10 => 1})
    end

    it "2 houses: (2 person, 8 used), (2 person, 10 used)" do
      houses = [[2, 8], [2, 10]]
      drying = Drying.new(houses)

      expect(drying.averages_per_capta).to eq({ 4 => 2 , 5 => 2})
    end

    it "2 houses: (2 person, 8 used), (2 person, 9 used)" do
      houses = [[2, 8], [2, 9]]
      drying = Drying.new(houses)

      expect(drying.averages_per_capta).to eq({ 4 => 4 })
    end

    it "3 houses: (3, 22), (2, 11), (3, 39)" do
      houses = [[3, 22], [2, 11], [3, 39]]
      drying = Drying.new(houses)

      expect(drying.averages_per_capta).to eq({ 5 => 2, 7 => 3, 13 => 3 })
    end
  end

  describe "average_total" do
    it "1 house: (1 person, 10 used)" do
      houses = [[1, 10]]
      drying = Drying.new(houses)

      expect(drying.average_total).to be_within(0.01).of(10.00)
    end

    it "1 house: (2 person, 10 used)" do
      houses = [[2, 10]]
      drying = Drying.new(houses)

      expect(drying.average_total).to be_within(0.01).of(5.00)
    end

    it "1 house: (3 person, 10 used)" do
      houses = [[3, 10]]
      drying = Drying.new(houses)

      expect(drying.average_total).to be_within(0.01).of(3.33)
    end

    it "2 houses: (1 person, 10 used), (2 person, 11 used)" do
      houses = [[1, 10], [2, 11]]
      drying = Drying.new(houses)

      expect(drying.average_total).to be_within(0.01).of(7.00)
    end

    it "3 houses: (3, 22), (2, 11), (3, 39)" do
      houses = [[3, 22], [2, 11], [3, 39]]
      drying = Drying.new(houses)

      expect(drying.average_total).to be_within(0.01).of(9.00)
    end
  end
end
