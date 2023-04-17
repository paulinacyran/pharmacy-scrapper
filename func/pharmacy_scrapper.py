from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from unidecode import unidecode
from func.helpers import wait_for_element


class PharmacyScrapper:
	def __init__(self, product):
		self.product = product
		self.driver = webdriver.Chrome(service=Service(os.path.join('chromedriver', 'chromedriver.exe')))
		self.product_dict = {}
    
	def accept_cookies(self, xpath):
		accept_cookies_btn_element = self.driver.find_element(By.XPATH, xpath)
		wait_for_element(self.driver, xpath)
		accept_cookies_btn_element.click()
       
	def search_product(self, xpath):
		search_engine_input_element = self.driver.find_element(By.XPATH, xpath)
		wait_for_element(self.driver, xpath)
		search_engine_input_element.click()
		search_engine_input_element.send_keys(self.product.lower() + Keys.ENTER)
		time.sleep(2)
       
	def check_gemini_pharmacy(self):
		# Website URL
		pharmacy_name = 'Gemini'
		url = 'https://gemini.pl/'
        
		# Open a website
		self.driver.get(url)
    
		# Accept cookies
		accept_cookies_btn_xpath = '//button[@class="button mb-1 is-base is-primary"]'
		self.accept_cookies(accept_cookies_btn_xpath)
    
		# Go to search engine and search for the product
		search_engine_input_xpath = '(//input[@class="w-full h-10 pl-4 pr-10 outline-none rounded-3xl text-14 truncate text-primary bg-primary-alternative placeholder-primary"])[1]'
		self.search_product(search_engine_input_xpath)
        
		# Add found items to the dictionary
		product_name_to_xref = unidecode(self.product).lower()
		for i in product_name_to_xref:
			if i in [" ", ",", ".", "-", ":"]:
				product_name_to_xref = product_name_to_xref.replace(i, "-")
		found_product_xpath = f'//div[@class="relative w-full p-2 rounded-lg transition bg-white text-black shadow-none hover:text-primary-action hover:shadow-product-card"]//a[contains(@class, "absolute inset-0 z-10") and contains(@href, {product_name_to_xref})]'
		found_product_elements = self.driver.find_elements(By.XPATH, found_product_xpath)
		found_product_price_xpath = '//div[@class="relative w-full p-2 rounded-lg transition bg-white text-black shadow-none hover:text-primary-action hover:shadow-product-card"]//span[@class="text-16 mr-2 font-bold"]'
		found_product_price_elements = self.driver.find_elements(By.XPATH, found_product_price_xpath)
    
		for i in range(len(found_product_elements)):
			found_product_name = found_product_elements[i].get_attribute('title')
			found_product_price = found_product_price_elements[i].get_attribute('innerText')
			found_product_website = found_product_elements[i].get_attribute('href')
			found_product_price = found_product_price.replace("\xa0zł", "")
			found_product_price = found_product_price.replace(",", ".")
			found_product_price = float(found_product_price)
	        
			self.product_dict[i] = {}
			self.product_dict[i]['Product name'] = found_product_name
			self.product_dict[i]['Pharmacy'] = pharmacy_name
			self.product_dict[i]['Product price [PLN]'] = found_product_price
			self.product_dict[i]['Product website'] = found_product_website
         
		# Close the browser
		self.driver.quit()
		        
		# Return the dictionary
		return self.product_dict

	def check_ziko_pharmacy(self):
		# Website URL
		pharmacy_name = 'Ziko'
		url = 'https://www.e-zikoapteka.pl/'
	    
		# Open a website
		self.driver.get(url)
		    
		# Accept cookies
		accept_cookies_btn_xpath = '//div[@class="btn btn-agree"]'
		self.accept_cookies(accept_cookies_btn_xpath)
		    
		# Go to search engine and search for the product
		search_engine_input_xpath = '//input[@id="main_search"]'
		self.search_product(search_engine_input_xpath)
    
		# Add found items to the dictionary
		product_name_to_xref = unidecode(self.product).lower()
		for i in product_name_to_xref:
			if i in [" ", ",", ".", "-", ":"]:
				product_name_to_xref = product_name_to_xref.replace(i, "-")
		found_product_xpath = f'//article[@class="tile product-tile  grid-3"]//a[contains(@class, "product-name-link") and contains(@href, {product_name_to_xref})]'
		found_product_elements = self.driver.find_elements(By.XPATH, found_product_xpath)
		found_product_price_xpath = '//article[@class="tile product-tile  grid-3"]//span[@class="price-value"]'
		found_product_price_elements = self.driver.find_elements(By.XPATH, found_product_price_xpath)
		    
		for i in range(len(found_product_elements)):
			found_product_name = found_product_elements[i].get_attribute('innerText')
			found_product_price = found_product_price_elements[i].get_attribute('innerText')
			found_product_website = found_product_elements[i].get_attribute('href')
			found_product_price = found_product_price.replace(" zł", "")
			found_product_price = found_product_price.replace(",", ".")
			found_product_price = float(found_product_price)
			        
			self.product_dict[i] = {}
			self.product_dict[i]['Product name'] = found_product_name
			self.product_dict[i]['Pharmacy'] = pharmacy_name
			self.product_dict[i]['Product price [PLN]'] = found_product_price
			self.product_dict[i]['Product website'] = found_product_website
		        
		# Close the browser
		self.driver.quit()
		    
		# Return the dictionary
		return self.product_dict

	def check_melissa_pharmacy(self):
		# Website URL
		pharmacy_name = 'Melissa'
		url = 'https://www.apteka-melissa.pl/'
		    
		# Open a website
		self.driver.get(url)
		    
		# Accept cookies
		accept_cookies_btn_xpath = '//button[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'
		self.accept_cookies(accept_cookies_btn_xpath)
		    
		# Go to search engine and search for the product
		search_engine_input_xpath = '//input[@id="sample2"]'
		self.search_product(search_engine_input_xpath)

		# Add found items to the dictionary
		product_name_to_xref = unidecode(self.product).lower()
		for i in product_name_to_xref:
			if i in [" ", ",", ".", "-", ":"]:
				product_name_to_xref = product_name_to_xref.replace(i, "-")
		found_product_xpath = f'//div[@class="prefixbox-product-container "]//a[contains(@class, "prefixbox-product-name") and contains(@href, {product_name_to_xref})]'
		found_product_elements = self.driver.find_elements(By.XPATH, found_product_xpath)
		found_product_price_xpath = f'//div[@class="prefixbox-product-container "]//a[contains(@class, "prefixbox-product-name") and contains(@href, {product_name_to_xref})]//following-sibling::div[@class="prefixbox-product-price"]//span'
		found_product_price_elements = self.driver.find_elements(By.XPATH, found_product_price_xpath)
		    
		for i in range(len(found_product_elements)):
			found_product_name = found_product_elements[i].get_attribute('innerText')
			found_product_price = found_product_price_elements[i].get_attribute('innerText')
			found_product_website = found_product_elements[i].get_attribute('href')
			found_product_price = found_product_price.replace(" zł", "")
			found_product_price = found_product_price.replace(",", ".")
			found_product_price = float(found_product_price)
			        
			self.product_dict[i] = {}
			self.product_dict[i]['Product name'] = found_product_name
			self.product_dict[i]['Pharmacy'] = pharmacy_name
			self.product_dict[i]['Product price [PLN]'] = found_product_price
			self.product_dict[i]['Product website'] = found_product_website
		        
		# Close the browser
		self.driver.quit()
		    
		# Return the dictionary
		return self.product_dict

	def check_aptelia_pharmacy(self):
		# Website URL
		pharmacy_name = 'Aptelia'
		url = 'https://www.aptelia.pl/'
		    
		# Open a website
		self.driver.get(url)
		    
		# Accept cookies
		accept_cookies_btn_xpath = '//a[@id="cookies__close"]'
		self.accept_cookies(accept_cookies_btn_xpath)
		    
		# Go to search engine and search for the product
		search_engine_input_xpath = '//input[@id="autocompleteSearch"]'
		self.search_product(search_engine_input_xpath)
     
		# Add found items to the dictionary
		product_name_to_xref = unidecode(self.product)
		for i in product_name_to_xref:
			if i in [" ", ",", ".", "-", ":"]:
				product_name_to_xref = product_name_to_xref.replace(i, "-")
		found_product_xpath = f'//div[@id="product-list"]//a[contains(@class, "link--dark-orange") and contains(@href, {product_name_to_xref})]'
		found_product_elements = self.driver.find_elements(By.XPATH, found_product_xpath)
		found_product_price_xpath = '//div[@id="product-list"]//span[@class="price"]'
		found_product_price_elements = self.driver.find_elements(By.XPATH, found_product_price_xpath)
    
		for i in range(len(found_product_elements)):
			found_product_name = found_product_elements[i].get_attribute('innerText')
			found_product_price = found_product_price_elements[i].get_attribute('textContent')
			found_product_website = found_product_elements[i].get_attribute('href')
			found_product_price = found_product_price.replace("zł", "")
			found_product_price = f'{found_product_price[0:-2]}.{found_product_price[-2:]}'
			found_product_price = float(found_product_price)
			        
			self.product_dict[i] = {}
			self.product_dict[i]['Product name'] = found_product_name
			self.product_dict[i]['Pharmacy'] = pharmacy_name
			self.product_dict[i]['Product price [PLN]'] = found_product_price
			self.product_dict[i]['Product website'] = found_product_website
		        
		# Close the browser
		self.driver.quit()
		    
		# Return the dictionary
		return self.product_dict

	def check_cefarm_pharmacy(self):
		# Website URL
		pharmacy_name = 'Cefarm24'
		url = 'https://www.cefarm24.pl/'
		    
		# Open a website
		self.driver.get(url)
		    
		# Accept cookies
		accept_cookies_btn_xpath = '//button[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'
		self.accept_cookies(accept_cookies_btn_xpath)
		    
		# Go to search engine and search for the product
		search_engine_input_xpath = '//input[@id="main_search"]'
		self.search_product(search_engine_input_xpath)
    
		# Add found items to the dictionary
		product_name_to_xref = unidecode(self.product)
		for i in product_name_to_xref:
			if i in [" ", ",", ".", "-", ":"]:
				product_name_to_xref = product_name_to_xref.replace(i, "-")
		found_product_xpath = f'//div[@class="product-tile  tile grid-3"]//figure//a[contains(@href, {product_name_to_xref})]'
		found_product_elements = self.driver.find_elements(By.XPATH, found_product_xpath)
		found_product_price_xpath = '//div[@class="product-tile  tile grid-3"]//div[@class="regular"]//span'
		found_product_price_elements = self.driver.find_elements(By.XPATH, found_product_price_xpath)
    
		for i in range(len(found_product_elements)):
			found_product_name = found_product_elements[i].get_attribute("href")[24:-5].replace("-", " ").capitalize()
			found_product_price = found_product_price_elements[i].get_attribute('textContent')
			found_product_website = found_product_elements[i].get_attribute('href')
			found_product_price = found_product_price.replace(" PLN", "")
			found_product_price = found_product_price.replace(",", ".")
			found_product_price = float(found_product_price)
			        
			self.product_dict[i] = {}
			self.product_dict[i]['Product name'] = found_product_name
			self.product_dict[i]['Pharmacy'] = pharmacy_name
			self.product_dict[i]['Product price [PLN]'] = found_product_price
			self.product_dict[i]['Product website'] = found_product_website
		        
		# Close the browser
		self.driver.quit()
		    
		# Return the dictionary
		return self.product_dict