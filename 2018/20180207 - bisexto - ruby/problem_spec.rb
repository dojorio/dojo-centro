require_relative 'problem'

describe "bisexto" do
  it "2000 é divisivel por 4 e por 400" do
    expect(bisexto(2000)).to eq(true)
  end
  it "2020 é divisivel por 4 e por 400" do
    expect(bisexto(2020)).to eq(true)
  end
  it "1967" do
  	expect(bisexto(1967)).to eq(false)
  end
end

