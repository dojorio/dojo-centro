require 'catraca'

describe Catraca do

  it "deve autorizar o passageiro comum caso tenha credito" do
    catraca = Catraca.new
    cartao = Cartao.new
    cartao.creditos = 100

    catraca.autorizar(cartao)
    catraca.autorizado.should be_true
  end

  it "não deve autorizar o passageiro comum caso não tenha credito" do
    catraca = Catraca.new
    cartao = Cartao.new
    cartao.creditos = 0

    catraca.autorizar(cartao)
    catraca.autorizado.should be_false
  end

  it "deve autorizar o passageiro idoso com liberação do motorista" do
    catraca = Catraca.new
    cartao_do_idoso = CartaoDeIdoso.new
    cartao_do_motorista = CartaoDeMotorista.new

    catraca.autorizar cartao_do_idoso, cartao_do_motorista
    catraca.autorizado.should be_true
  end

  it "deve autorizar o estudante com liberação do motorista com crédito e dentro do horário" do
    catraca = Catraca.new
    cartao_do_estudante = CartaoDeEstudante.new
    cartao_do_estudante.creditos = 200

    cartao_do_motorista = CartaoDeMotorista.new

    catraca.autorizar cartao_do_estudante, cartao_do_motorista
    catraca.autorizado.should be_true
  end


    it "não deve autorizar o estudante com liberação do motorista sem crédito e dentro do horário" do
    catraca = Catraca.new
    cartao_do_estudante = CartaoDeEstudante.new
    cartao_do_estudante.creditos = 0

    cartao_do_motorista = CartaoDeMotorista.new

    catraca.autorizar cartao_do_estudante, cartao_do_motorista

    catraca.autorizado.should be_false
  end






end

