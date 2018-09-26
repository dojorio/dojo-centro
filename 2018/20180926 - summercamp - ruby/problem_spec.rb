require_relative 'problem'

describe "gincana" do
  it "Ma4 Pe3 Jo2 vence Pe" do
    criancas = {Ma:4, Pe:3, Jo:2}
    expect(gincana(criancas)).to eq("Pe")
  end

  it "Pe3 Ma4 Jo2 vence Jo" do
    criancas = {Pe:3, Ma:4, Jo:2}
    expect(gincana(criancas)).to eq("Jo")
  end
end
