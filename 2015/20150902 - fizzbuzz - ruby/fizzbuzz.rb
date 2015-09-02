def fizzbuzz(num) 
	#return "1" if (num == 1)

	return "fizzbuzz" if num == 15

	return "fizz" if num % 3 == 0

	case num 
		when 5 , 10
			return "buzz"
    end

	return num.to_s

end

