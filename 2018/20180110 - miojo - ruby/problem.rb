def problem(amp1,amp2)

	return 3 if amp1 == 3 || amp2 ==3

	if [amp1, amp2].max() - [amp1, amp2].min() >= 3
       return [amp1, amp2].max()
	end
  
  return 8
  
end