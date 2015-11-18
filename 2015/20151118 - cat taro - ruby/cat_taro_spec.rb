require './cat_taro'

describe "Cat Taro" do
  it "is possible to CAT" do
    expect(cat_taro("CAT")).to eq("Possible")
  end

  it "is impossible to C" do
    expect(cat_taro("C")).to eq("Impossible")
  end

  it "is impossible to A" do
    expect(cat_taro("A")).to eq("Impossible")
  end

  it "is impossible to CA" do
    expect(cat_taro("CA")).to eq("Impossible")
  end

  it "is impossible to B" do
    expect(cat_taro("B")).to eq("Impossible")
  end

  it "is impossible to X" do
    expect(cat_taro("X")).to eq("Impossible")
  end

  it "is possible to XCAT" do
    expect(cat_taro("XCAT")).to eq("Possible")
  end

  it "is possible to XCAET" do
    expect(cat_taro("XCAET")).to eq("Possible")
  end

  it "is impossible to XCAAET" do
    expect(cat_taro("XCAAET")).to eq("Impossible")
  end

  it "is impossible to XCAETT" do
    expect(cat_taro("XCAETT")).to eq("Impossible")
  end

  it "is impossible to XCCAET" do
    expect(cat_taro("XCCAET")).to eq("Impossible")
  end

  it "is impossible to TAC" do
    expect(cat_taro("TAC")).to eq("Impossible")
  end

  it "is impossible to ACT" do
    expect(cat_taro("ACT")).to eq("Impossible")
  end

  it "is impossible to ATC" do
    expect(cat_taro("ATC")).to eq("Impossible")
  end

  it "is impossible to TCA" do
    expect(cat_taro("TCA")).to eq("Impossible")
  end

  it "is impossible to CTA" do
    expect(cat_taro("TCA")).to eq("Impossible")
  end

  it "is possible to SGHDJHFIOPUFUHCHIOJBHAUINUIT" do
    expect(cat_taro("SGHDJHFIOPUFUHCHIOJBHAUINUIT")).to eq("Possible")
  end    

  it "is possible to XCYAZTX" do
    expect(cat_taro("XCYAZTX")).to eq("Possible")
  end
end