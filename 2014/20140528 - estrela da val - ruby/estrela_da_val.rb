require 'prime'

def estrela_da_val(pontos)
   if Prime.prime?(pontos)
     return pontos / 2
   end

   case pontos
   when 8, 10, 12
     2
   when 9
     3
   else
     1
   end

   

end