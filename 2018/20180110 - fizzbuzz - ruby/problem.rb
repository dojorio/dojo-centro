def fizzbuzz(num)
	if num % 15 == 0
		return "fizzbuzz"
	end
	if num % 3 == 0
		return "fizz"
	end
	if num % 5 == 0
		return "buzz"
	end
	num
end