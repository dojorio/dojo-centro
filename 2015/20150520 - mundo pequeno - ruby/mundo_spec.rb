require './mundo'

describe "Mundo pequeno" do
  context "com todos os amigos perto" do
    let(:amigos) do
      { 
        A: [0, 0] ,
        B: [1, 0],
        C: [0, 1],
        D: [-1, 0] 
      }
    end

    it "Visito A" do
      expect(povo_perto(amigos, :A))
        .to match_array([:B, :C, :D])
    end

    it "Visito D" do 
      expect(povo_perto(amigos, :D))
        .to match_array([:A, :B, :C])
    end

    it "Visito C" do 
      expect(povo_perto(amigos, :C))
        .to match_array([:A, :B, :D])
    end
  end

  context "com um amigo longe" do
    let(:amigos) do
      { 
        A: [0, 0],
        B: [1, 0],
        C: [0, 1],
        D: [-1, 0],
        E: [1, 1] 
      }
    end

    it "Visito A" do
      expect(povo_perto(amigos, :A))
        .to match_array([:B, :C, :D])
    end

    it "Visito E" do
      expect(povo_perto(amigos, :E))
        .to match_array([:A, :B, :C])
    end
    
    it "Visito B" do
      expect(povo_perto(amigos, :B))
        .to match_array([:A, :C, :E])
    end
  end

  context "com dois amigos longe" do
    let(:amigos) do
      { 
        A: [0, 0],
        B: [1, 0],
        C: [0, 1],
        D: [-1, 0],
        E: [1, 1],
        F: [10, 1] 
      }
    end

    it "Visito A" do
      expect(povo_perto(amigos, :A))
        .to match_array([:B, :C, :D])
    end

    it "Visito E" do
      expect(povo_perto(amigos, :E))
        .to match_array([:A, :B, :C])
    end

    it "Visito B" do
      expect(povo_perto(amigos, :B))
        .to match_array([:A, :C, :E])
    end

    it "Visito C" do
      expect(povo_perto(amigos, :C))
        .to match_array([:A, :B, :E])
    end
  end
end