require 'saving_time'

describe "Saving Time" do

  describe "Minutes" do


    it "12:00" do
      posicao_do_ponteiro_em("12:00").should == [0,0]
    end

    it "12:08" do
      posicao_do_ponteiro_em("12:08").should == [0,2]
    end

    it "12:05" do
      posicao_do_ponteiro_em("12:05").should == [0,1]
    end

    it "12:15" do
      posicao_do_ponteiro_em("12:15").should == [0,3]
    end

    it "12:20" do
      posicao_do_ponteiro_em("12:20").should == [0,4]
    end

    it "12:07" do
      posicao_do_ponteiro_em("12:07").should == [0,1]
    end

    it "12:09" do
      posicao_do_ponteiro_em("12:09").should == [0,2]
    end

    it "12:29" do
      posicao_do_ponteiro_em("12:29").should == [0,6]
    end

    it "11:59" do
      posicao_do_ponteiro_em("11:59").should == [0,0]
    end

  end

  describe "Houres" do
    it "12:59" do
      posicao_do_ponteiro_em("12:59").should == [1,0]
    end
  end
end

