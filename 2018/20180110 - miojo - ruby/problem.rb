def problem(amp1,amp2)
	if [amp1, amp2].max() - [amp1, amp2].min()
       return [amp1, amp2].max()
	end
  
  return [amp1, amp2].max() 
end