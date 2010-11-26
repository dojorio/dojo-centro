class Catraca
  attr_accessor :autorizado
  def autorizar(cartao, cartao_autorizador = nil)
    if cartao_autorizador
        @autorizado = true
    else
      @autorizado = cartao.creditos > 0
    end
  end
end

class Cartao
  attr_accessor :creditos
end

class CartaoDeIdoso < Cartao
  @creditos = 0
end

class CartaoDeEstudante < Cartao
    @horario_permitido = [,]
end

class CartaoDeMotorista < Cartao
end

