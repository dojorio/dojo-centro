require './miojo.rb'

describe "Miojo" do
  it "miojo de 1 minuto 2 ampulhetas 2 e 3 minutos" do
    miojo = 1
    ampulhetas = [2, 3]

    expect(tempo_preparo(miojo, ampulhetas)).to eq(3)
  end

  it "miojo de 2 minutos e ampulhetas de 3 e 5" do
    miojo = 2
    ampulhetas = [3, 5]
    expect(tempo_preparo(miojo, ampulhetas)).to eq(5)
  end

  it "miojo de 1 minuto e ampulhetas de 3 e 4" do
    miojo = 1
    ampulhetas = [3, 4]
    expect(tempo_preparo(miojo, ampulhetas)).to eq(4)
  end

  it "miojo de 1 minuto e ampulhetas de 4 e 3" do
    miojo = 1
    ampulhetas = [4, 3]
    expect(tempo_preparo(miojo, ampulhetas)).to eq(4)
  end

  it "miojo de 1 minutos e ampulhetas de 3 e 5" do
    miojo = 1
    ampulhetas = [3, 5]
    expect(tempo_preparo(miojo, ampulhetas)).to eq(6)
  end

  it "miojo de 2 minutos e ampulhetas de 3 e 4" do
    miojo = 2
    ampulhetas = [3, 4]
    expect(tempo_preparo(miojo, ampulhetas)).to eq(6)
  end

  it "miojo de 3 minutos e ampulhetas de 5 e 7" do
    miojo = 3
    ampulhetas = [5, 7]
    expect(tempo_preparo(miojo, ampulhetas)).to eq(10)
  end

  it "miojo de 3 minutos e ampulhetas de 7 e 5" do
    miojo = 3
    ampulhetas = [7, 5]
    expect(tempo_preparo(miojo, ampulhetas)).to eq(10)
  end

  it "miojo de 2 minutos e ampulhetas de 3 e 8" do
    miojo = 2
    ampulhetas = [3, 8]
    expect(tempo_preparo(miojo, ampulhetas)).to eq(8)
  end

  it "miojo de 2 minutos e ampulhetas de 3 e 3" do
    miojo = 2
    ampulhetas = [3, 3]
    expect(tempo_preparo(miojo, ampulhetas)).to eq("Pizza")
  end

  it "miojo de 1 minuto e ampulhetas de 3 e 10" do
    miojo = 1
    ampulhetas = [3, 10]
    expect(tempo_preparo(miojo, ampulhetas)).to eq(10)
  end

  it "miojo de 1 minuto e ampulhetas de 3 e 8" do
    miojo = 1
    ampulhetas = [3, 8]
    expect(tempo_preparo(miojo, ampulhetas)).to eq(9)
  end

  it "miojo de 10 minuto e ampulhetas de 30 e 80" do
    miojo = 10
    ampulhetas = [30, 80]
    expect(tempo_preparo(miojo, ampulhetas)).to eq(90)
  end

  it "miojo de 3 minuto e ampulhetas de 4 e 6" do
    miojo = 3
    ampulhetas = [4, 6]
    expect(tempo_preparo(miojo, ampulhetas)).to eq("Pizza")
  end
  
end