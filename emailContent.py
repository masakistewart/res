def contentCreator(position, firstName, companyName, reason):
	return "Hello {0},\n\nMy name is Cairo. I noticed that you have a {1} position open and I'd like to chat about working at {2}. I have a background in Node.js and Angular. {3}.\nPlease let me know what time is good for you my number is 415 793 - 4319.\n\nThanks,\n\nCairo Stewart".format(firstName, position, companyName, reason)

def reasonCreator(companyType):
	types = {
		"gaming": "I was and still am an Avid gamer. I would really like to work for a company that I enjoy the product of",
		"green": "Growing up in the bay area and going to school in a lead certified building I understand and appreciate the environment and would like to continue helping out our planet Earth!",
		"startup": "Helping small businesses getting off their feet and onto the web is something has given me a lot of happiness in the past."
	}
	return types[companyType]