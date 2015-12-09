require_relative 'animal_game'

describe "Animal game" do
  it "gives zero if no combination is found" do
    expect(prize(1, 1234, 0)).to eq(0)
  end

  context "gives 16x value if is from same group" do
    it "1" do
      expect(prize(1, 1299, 0)).to eq(16)
    end

    it "2" do
      expect(prize(2, 1299, 0)).to eq(32)
    end

    it "3" do
      expect(prize(2, 1297, 0)).to eq(32)
    end

    it "4" do
      expect(prize(2, 1201, 2)).to eq(32)
    end

    it "5" do
      expect(prize(2, 1205, 7)).to eq(32)
    end

    it "6" do
      expect(prize(2, 1205, 3)).to eq(0)
    end

    it "7" do
      expect(prize(2, 3405, 3)).to eq(0)
    end

    it "8" do
      expect(prize(2, 3405, 1206)).to eq(32)
    end

    it "9" do
      expect(prize(2, 1200, 5601)).to eq(0)
    end

    it "10" do
      expect(prize(2, 1200, 5699)).to eq(32)
    end
  end

  context "gives 50x if last 2 digits are equal" do
    it "1" do
      expect(prize(2, 1299, 5699)).to eq(100)
    end

    it "2" do
      expect(prize(2, 1299, 5699)).to eq(100)
    end

  end

  context "gives 500x if last 3 digits are equal" do
    it "1" do
      expect(prize(2, 1299, 5299)).to eq(1000)
    end
  end

  context "gives 3000x if last 4 digits are equal" do
    it "1" do
      expect(prize(2, 5299, 5299)).to eq(6000)
    end
  end

  it "from definition" do
    expect(prize(32.20, 32, 213929)).to eq( 515.20)
    expect(prize(10.50, 32, 213032)).to eq(5250.00)
    expect(prize(2000.00, 340000, 0)).to eq(6000000.00)
    expect(prize(520.00, 874675, 928567)).to eq(0.00)
    expect(prize(10.00, 1111, 578311)).to eq(500.00)
  end

end