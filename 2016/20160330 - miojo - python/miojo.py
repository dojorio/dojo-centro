def miojo(amp1, amp2):
	if (amp1 == 1 or amp2 == 1 or amp1 == 3 or amp2 == 3):
		return 3

	return max(amp1, amp2)