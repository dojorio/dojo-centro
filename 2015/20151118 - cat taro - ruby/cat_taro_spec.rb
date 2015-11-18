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

end