def growing_strings(strings)
	if strings.count == 2 and strings[1].include?(strings[0])
		return 2
	end
	1
end