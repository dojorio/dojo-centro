
def destroy(stars):
	if len(stars) == 3:
		return stars[0] * stars[2]

	maior_produto = 0
	for index, _ in enumerate(stars[1:-1], start=1):
		produto = stars[index - 1] * stars[index + 1]
		if produto > maior_produto:
			sai = index
			maior_produto = produto



	stars.pop(sai)
	return (stars[sai-1]*stars[sai]) + destroy(stars)