require "miojo"

describe "Miojo de 1 min" do
  let(:miojo){ 1 }
  
  it "deve ficar pronto em 3 min com apulhetas de 3 e 2min" do
    ampulhetas = [2, 3]
    tempo_minimo_de_preparo(miojo, ampulhetas).should == 3
  end
  
  it "deve ficar pronto em 4 min com apulhetas de 4 e 3min" do
    ampulhetas = [3, 4]
    tempo_minimo_de_preparo(miojo, ampulhetas).should == 4
  end
  
  it "deve ficar pronto em 6 min com apulhetas de 5 e 3min" do
    ampulhetas = [3, 5]
    tempo_minimo_de_preparo(miojo, ampulhetas).should == 6
  end

  it "deve ficar pronto em 5 min com apulhetas de 2 e 5min" do
    ampulhetas = [2, 5]
    tempo_minimo_de_preparo(miojo, ampulhetas).should == 5
  end

 it "nunca ficara pronto com apulhetas de 2 e 2min" do
    ampulhetas = [2, 2]
    tempo_minimo_de_preparo(miojo, ampulhetas).should be false
  end
  
  it "nunca ficara pronto com apulhetas de 2 e 4min" do
    ampulhetas = [2, 4]
    tempo_minimo_de_preparo(miojo, ampulhetas).should be false
  end
  
  it "nunca ficara pronto com apulhetas de 3 e 6min" do
    ampulhetas = [3, 6]
    tempo_minimo_de_preparo(miojo, ampulhetas).should be false
  end
 
  
end

describe "Miojo de 2 min" do
  let(:miojo){ 2 }
  
  it "deve ficar pronto em 22 min com apulhetas de 10 e 11min" do
    ampulhetas = [10, 11]
    tempo_minimo_de_preparo(miojo, ampulhetas).should == 22
  end
end

describe "Miojo de 3 min" do
  let(:miojo){ 3 }
  
  it "deve ficar pronto em 7 min com apulhetas de 4 e 7min" do
    ampulhetas = [4, 7]
    tempo_minimo_de_preparo(miojo, ampulhetas).should == 7
  end
  
  it "deve ficar pronto em 10 min com apulhetas de 5 e 7min" do
    ampulhetas = [5, 7]
    tempo_minimo_de_preparo(miojo, ampulhetas).should == 10
  end
end

describe "Miojo de 4 min" do
  let(:miojo){ 4 }
  
  it "deve ficar pronto em 14 min com ampulhetas de 5 e 7min" do
    ampulhetas = [5, 7]
    tempo_minimo_de_preparo(miojo, ampulhetas).should == 14
  end
  
  it "deve ficar pronto em 24 min com ampulhetas de 5 e 8min" do
    ampulhetas = [5, 8]
    tempo_minimo_de_preparo(miojo, ampulhetas).should == 20
  end
end

