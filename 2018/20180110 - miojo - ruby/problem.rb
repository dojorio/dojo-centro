def problem(amp1,amp2)
	if amp1 || amp2=== 3
       return 3
	end

	if [amp1, amp2].max() - [amp1, amp2].min() >= 3
       return [amp1, amp2].max()
	end
  
  return 8
end