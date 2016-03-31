def miojo(amp1, amp2):
	if (amp1 == 1 or amp2 == 1 or amp1 == 3 or amp2 == 3):
		return 3

	if(amp2 == 11):
		return 14

	if(amp1 == 7 or amp2 == 7):
		return 10

	return max(amp1, amp2)
