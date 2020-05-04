import uuid
from selenium import webdriver
import time
import shutil

class ChromeBrowserWorker:

	def init_driver(self):
		options = webdriver.ChromeOptions()
		options.add_argument("user-data-dir=sessions/{0}".format(self.session_id))
		return webdriver.Chrome(options=options)

	def __init__(self):
		self.session_id = uuid.uuid4()
		self.driver = self.init_driver() 

	def click_element(self, element, selector):
		element = self.driver.find_element_by_xpath("//{0}[text() = '{1}']".format(element, selector))
		element.click()
		time.sleep(3)

	def element_is_present(self, element, selector):
		try:
			element = self.driver.find_element_by_xpath("//{0}[text() = '{1}']".format(element, selector))
			return True
		except Exception as e:
			return False


	def type_text(self, type, input_text):
		input_element = self.driver.find_element_by_xpath("//input[@type = '{0}']".format(type))
		input_element.click()
		input_element.send_keys(input_text)

	def navigate_to(self, path):
		self.driver.get(path)

	def quit(self):
		self.driver.quit()
		# need to sleep to allow current process to close file descriptors to sessions directory
		time.sleep(1)
		shutil.rmtree("sessions".format(self.session_id))