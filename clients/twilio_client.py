from twilio.rest import Client


class TwilioClient:

	def __init__(self, config):
		self.sender = config["sender"]
		self.client = Client(config["account_sid"], config["auth_token"])


	def send_text(self, reciever, body):
		message = self.client.messages.create(
		    to=reciever, 
		    from_=self.sender,
		    body=body)

		print("text message sent!")