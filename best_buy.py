import sys
from browserworkers import ChromeBrowserWorker
from clients import TwilioClient
from bots import BestBuyBot
import yaml

def load_config():
	with open("config.yml", "r") as ymlfile:
		return yaml.load(ymlfile, Loader=yaml.FullLoader)

if __name__ == "__main__":
	config = load_config()
	worker = ChromeBrowserWorker()
	texter = TwilioClient(config["twilio"])
	bot = BestBuyBot(worker, texter, config["best_buy"])
	target = sys.argv[1]
	text_reciever = sys.argv[2]
	bot.run(target, text_reciever)