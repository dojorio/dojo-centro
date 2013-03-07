require "trilha"

describe "Trilha" do

  context "em um dia" do
    let(:dias) { 1 }

    it "vazia" do
      trilha([], dias).should eq(0)
    end

    it "e com dois acampamentos" do
      trilha([2], dias).should eq(2)
    end

    it "e com três acampamentos" do
      trilha([2, 3], dias).should eq(5)
    end

    it "e com quatro acampamentos" do
      trilha([2, 3, 4], dias).should eq(9)
    end
  end


  context "em dois dias" do
    let(:dias) { 2 }

    it "e com dois acampamentos" do
      trilha([2], dias).should eq(2)
    end

    context "com três acampamentos" do
      it { trilha([2, 3], dias).should eq(3) }
      it { trilha([2, 4], dias).should eq(4) }
      it { trilha([2, 4, 1], dias).should eq(5) }
    end

    context "com três acampamentos" do
      it { trilha([3, 4, 1], dias).should eq(5) }
      it { trilha([3, 4, 2], dias).should eq(6) }
      it { trilha([2, 4, 3], dias).should eq(6) }
    end

    context "com cinco acampamentos" do
      it { trilha([3, 2, 2, 3], dias).should eq(5) }
      it { trilha([4, 2, 2, 4], dias).should eq(6) }
      it { trilha([1, 1, 1, 4], dias).should eq(4) }
      it { trilha([1, 1, 1, 9], dias).should eq(9) }
      it { trilha([1, 1, 1, 5], dias).should eq(5) }
      it { trilha([5, 1, 1, 1], dias).should eq(5) }
      it { trilha([1, 5, 1, 1], dias).should eq(6) }
    end
  end

  context "em três dias" do
    let(:dias) { 3 }

    context "e com cinco acampamentos" do
      it { trilha([1, 5, 1, 1], dias).should eq(5) }
      it { trilha([1, 6, 1, 1], dias).should eq(6) }
      it { trilha([1, 1, 6, 1], dias).should eq(6) }
    end

    it "e com seis acampamentos" do
      trilha([1, 1, 2, 2, 1], dias).should eq(3)
    end
  end
end
