import emailContent
import emailAddr
import sender


def main(firstName, lastName, position, companyName, companyType):
	addressArr = emailAddr.createEmail(firstName, lastName, companyName)
	reason	 = emailContent.reasonCreator(companyType)
	content  = emailContent.contentCreator(position, firstName, companyName, reason)
	sender.send(addressArr, content, position)
	print("sent to ", addressArr)

main("ariflo", "flores", "full stack", "arianflores", "green")