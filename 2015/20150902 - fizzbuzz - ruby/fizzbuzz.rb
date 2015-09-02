def fizzbuzz(num) 
	#return "1" if (num == 1)

	case num 
		when 3 , 6, 9
			return "fizz"
		when 5 , 10
			return "buzz"
    end

	return num.to_s

end

