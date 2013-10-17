# -*- coding: utf-8 -*-

def lt_eq(a, b) 
	a < b || (a - b).abs < 1e-6
end

def xihs(r, h)
	2*Math.sqrt(r**2 - h**2/4.0)
end

def paintball(altura, largura, verdes, vermelhas)
	return false if verdes.empty? and vermelhas.empty?

	if verdes.any? && vermelhas.any?
		lt_eq(largura, xihs(verdes.first, altura) + 
					   xihs(vermelhas.first, altura)) ? 2 : false
	elsif verdes.any?
		lt_eq(largura, xihs(verdes.first, altura)) ? 1 : false
	elsif vermelhas.any?
		lt_eq(largura, xihs(vermelhas.first, altura)) ? 1 : false
	end
end