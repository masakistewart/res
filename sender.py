import requests

def send(addressArr, content, position):
	return requests.post(
        "https://api.mailgun.net/v3/sandbox2853b4a6d48f4929854a46ee8ecaa21f.mailgun.org/messages",
        auth=("api", "key-5d1469b48e24752d65dc0f775555055e"),
        data={"from": "cairomstewart@gmail",
              "to": addressArr,
              "subject": position,
              "text": content})