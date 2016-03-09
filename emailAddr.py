def createEmail(firstName,lastName,companyName):
	dot = "."
	d = "@" + companyName + ".com"
	return [firstName + dot + lastName + d, firstName + lastName + d, firstName[0] + dot + lastName + d, firstName + d, lastName + dot + firstName + d]