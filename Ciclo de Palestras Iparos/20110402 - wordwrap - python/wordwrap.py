class NotWrappableError(Exception):
	pass

def wordwrap(text, width):
	if len(text) <= width:
		return text
	else:
		cut = width
		
		if " " in text:
			space_position = text.find(" ")
			cut = min(space_position + 1, width)

		return text[:cut].strip() + "\n" + wordwrap(text[cut:].strip(), width)