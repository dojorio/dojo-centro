def volume_extra(pedido, estoque)
  if pedido[0][0] == 2 || pedido[0][1] == 2 || pedido[0][2] == 2
     
        if estoque[0][0] != 2 && estoque[0][1] != 2 && estoque[0][2] != 2
          return "error"
        end

         if pedido[0][0] == 2 && pedido[0][1] == 2 && estoque[0][1] != 2
          return "error"
    end
  end

  return 0
end