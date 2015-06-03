require './dependencias'

describe "dependencias" do
  it "returns simple dependencies" do
    expect(dependencias(A: [:B])).to eq(A: [:B])
  end

  it "returns simple dependencies 2" do
    expect(dependencias(A: [:C])).to eq(A: [:C])
  end

  it "returns ordered dependencies" do
    expect(dependencias(A: [:C, :B])).to eq(A: [:B, :C])
  end

  it "returns sorted dependencies" do
    expect(dependencias(B: [:C, :A])).to eq(B: [:A, :C])
  end

  it "returns dependencies to all classes" do
    expect(dependencias(A: [:C], B: [:C])).to eq(A: [:C], B: [:C])
  end

  it "returns sorted dependencies to all classes" do
    expect(dependencias(A: [:C, :B], B: [:C])).to eq(A: [:B, :C], B: [:C])
  end

  it "returns simple transitivity" do
    expect(dependencias(A: [:B], B: [:C])).to eq(A: [:B, :C], B: [:C])
  end

  it "returns simple transitivity 2" do
    expect(dependencias(A: [:D, :B], B: [:C])).to eq(A: [:B, :C, :D], B: [:C])
  end

  it "returns composite transitivity" do
    expect(dependencias(A: [:D, :B], B: [:C], C: [:E])).to eq(A: [:B, :C, :D, :E], B: [:C,:E], C: [:E])
  end

  it "returns direitinho" do
    entrada = { A: [:B, :C],
    B: [:C, :E],
    C: [:G],
    D: [:A, :F],
    E: [:F],
    F: [:H] }

    saida = { A: [:B, :C, :E, :F, :G, :H],
    B: [:C, :E, :F, :G, :H],
    C: [:G],
    D: [:A, :B, :C, :E, :F, :G, :H],
    E: [:F, :H],
    F: [:H] }

    expect(dependencias(entrada)).to eq(saida)
  end
end