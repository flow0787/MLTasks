import sqlite3

conn = sqlite3.connect('ipaddresses.db')

c = conn.cursor()

c.execute("""CREATE TABLE ipaddresses (
	  date text,
	  region_code integer,
	  country_name text,
	  longitude text,
	  latitude text,
	  city text,
	  continent_name text,
	  country_code text,
	  location blob,
	  type text,
	  ip text,
	  zip integer,
	  continent_code text,
	  region_name text
	  )""")

conn.commit()
conn.close()
