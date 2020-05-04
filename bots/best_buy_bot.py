import time
import re


class BestBuyBot:

	BASE_URL = "https://www.bestbuy.com"
	SIGN_IN_URL = BASE_URL + "/signin"
	CHECKOUT_FAST_TRACK = BASE_URL + "/checkout/r/fast-track"
	SUCCESS_MESSAGE = "item successfully purchased. Head on over to https://www.bestbuy.com/signin to proceed."


	URL_DICT = {
		"grey": BASE_URL + "/site/nintendo-switch-32gb-console-gray-joy-con/6364253.p?skuId=6364253",
		"neon": BASE_URL + "/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255.p?skuId=6364255",
		"ac": BASE_URL + "/site/nintendo-switch-animal-crossing-new-horizons-edition-32gb-console-multi/6401728.p?skuId=6401728",
		"test": BASE_URL + "/site/animal-crossing-new-horizons-nintendo-switch/5723316.p?skuId=5723316"
	}

	def __init__(self, worker, texter, config):
		self.worker = worker
		self.texter = texter
		self.user = config["user"]
		self.password = config["password"]

	def parse_url(self, target):
		if re.search("https?:\/\/", target):
			return target
		if self.URL_DICT[target]:
			return self.URL_DICT[target]
		raise ValueError("invalid target for bot")

	def log_in(self):
		self.worker.navigate_to(self.SIGN_IN_URL)
		self.enter_sign_in_creds()

	def add_to_cart(self, url):
		self.worker.navigate_to(url)
		self.worker.click_element('button', 'Add to Cart')

	def added_to_cart(self):
		return self.worker.element_is_present('span', 'Place Your Order')

	def enter_sign_in_creds(self):
		self.worker.type_text('email', self.user)
		self.worker.type_text('password', self.password)
		self.worker.click_element('button', 'Sign In')

	def run(self, target, text_reciever):
		url = self.parse_url(target)
		try:
			self.log_in()
			while True:
				try:
					self.add_to_cart(url)
				except Exception as e:
					print("Could not add to cart: \n", e)
					continue
				self.worker.navigate_to(self.CHECKOUT_FAST_TRACK)
				if self.added_to_cart() and text_reciever:
					self.texter.send_text(text_reciever, self.SUCCESS_MESSAGE)
					break
				time.sleep(1)
		finally:
			self.worker.quit()

