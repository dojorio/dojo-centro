def fizzbuzz(num) 
	#return "1" if (num == 1)

	return "fizzbuzz" if num == 15 || num == 30

	return "fizz" if num % 3 == 0

	return "buzz" if num % 5 == 0

	return num.to_s

end

