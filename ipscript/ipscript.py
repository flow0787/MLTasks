import requests
import sqlite3
import datetime
import time

#IP = str(sys.argv[1])

IP = requests.get('https://api.ipify.org').text
#print(IP)

#api key
KEY = '1a0f0bab1df3628ba01f6d13558854ae'

URL = 'http://api.ipstack.com/{}?access_key={}&format=1'.format(IP,KEY)
#print(URL)

current_time = datetime.datetime.now()


r = requests.get(URL)
result = r.json()



while True:
	conn = sqlite3.connect('ipaddresses.db')
	c = conn.cursor()

	for key, value in result.items():
		if key == 'region_code':
			c.execute('''INSERT INTO ipaddresses (date) VALUES (?)''', (current_time,))
			conn.commit()
			region_code_value = result.get(key)
			c.execute('''INSERT INTO ipaddresses (region_code) VALUES (?)''', (region_code_value,))
			conn.commit()
		if key == 'country_name':
			country_name_value = result.get(key)
			c.execute('''INSERT INTO ipaddresses (country_name) VALUES (?)''', (country_name_value,))
			conn.commit()
		if key == 'longitude':
			longitude_value = result.get(key)
			c.execute('''INSERT INTO ipaddresses (longitude) VALUES (?)''', (longitude_value,))
			conn.commit()
		if key == 'latitude':
			latitude_value = result.get(key)
			c.execute('''INSERT INTO ipaddresses (latitude) VALUES (?)''', (latitude_value,))
			conn.commit()
		if key == 'city':
			city_value = result.get(key)
			c.execute('''INSERT INTO ipaddresses (city) VALUES (?)''', (city_value,))
			conn.commit()
		if key == 'continent_name':
			continent_name_value = result.get(key)
			c.execute('''INSERT INTO ipaddresses (continent_name) VALUES (?)''', (continent_name_value,))
			conn.commit()
		if key == 'country_code':
			country_code_value = result.get(key)
			c.execute('''INSERT INTO ipaddresses (country_code) VALUES (?)''', (country_code_value,))
			conn.commit()
		if key == 'location':
			location_value = result.get(key)
			location_value = str(location_value)
			c.execute('''INSERT INTO ipaddresses (location) VALUES (?)''', (location_value,))
			conn.commit()
		if key == 'type':
			type_value = result.get(key)
			c.execute('''INSERT INTO ipaddresses (type) VALUES (?)''', (type_value,))
			conn.commit()
		if key == 'ip':
			ip_value = result.get(key)
			c.execute('''INSERT INTO ipaddresses (ip) VALUES (?)''', (ip_value,))
			conn.commit()
		if key == 'zip':
			zip_value = result.get(key)
			c.execute('''INSERT INTO ipaddresses (zip) VALUES (?)''', (zip_value,))
			conn.commit()
		if key == 'continent_code':
			continent_code_value = result.get(key)
			c.execute('''INSERT INTO ipaddresses (continent_code) VALUES (?)''', (continent_code_value,))
			conn.commit()
		if key == 'region_name':
			region_name_value = result.get(key)
			c.execute('''INSERT INTO ipaddresses (region_name) VALUES (?)''', (region_name_value,))
			conn.commit()
	conn.close()
	time.sleep(60)


