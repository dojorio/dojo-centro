def volume_extra(pedido, estoque)

  if pedido[0][0]==2 || pedido[0][1]==2 || pedido[0][2]==2
    return "error"
  end

  return 0
end