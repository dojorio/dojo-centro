# -*- coding: utf-8 -*-

def remendo(furos, tamanho, r1, r2)
	return 0 if furos.empty?

	r1,r2 = r2,r1 if r1 > r2 # Swap

	return r1 if furos.count == 1

	Δfuros = [furos.last - furos.first, (furos.first - furos.last) % tamanho].min

	resto_todo = r1 >= Δfuros ? r1 : 
				 r2 >= Δfuros ? r2 : tamanho

	resto_r1 = furos.reject{|x|x<=furos.first+r1}
	resto_r2 = furos.reject{|x|x<=furos.first+r2}
	
	resto_r3 = furos.reject{|x|x<=furos.first-r1}
	resto_r4 = furos.reject{|x|x<=furos.first-r2}

	[resto_todo, 
		r1 + remendo(resto_r1, tamanho, r1, r2),
		r2 + remendo(resto_r2, tamanho, r1, r2)].min
end