#!/usr/bin/python
# -*- coding: utf-8
from string import find
from string import replace
from imposm.parser import OSMParser
# simple class that handles the parsed OSM data.

class institutions_filler(object):
	shops = []
	def fill_institutions(self, node):
		for institution in node:
			if 'shop' in institution[1]:
				self.shops.append(institution)

# instantiate counter and parser and start parsing
counter = institutions_filler()
p = OSMParser(concurrency=4, nodes_callback=counter.fill_institutions)
p.parse('RU.osm.pbf')


import MySQLdb
import string

# подключаемся к базе данных (не забываем указать кодировку, а то в базу запишутся иероглифы)
db = MySQLdb.connect(host="localhost", user="root", passwd="GnbweTv]", db="test", charset='utf8')
# формируем курсор, с помощью которого можно исполнять SQL-запросы
cursor = db.cursor()
                
for shop in counter.shops:
	# подставляем эти данные в SQL-запрос
	sql = """INSERT INTO institutions VALUES(%(osm_id)d, '%(name)s', %(latitude)f, %(longitude)f)"""\
	%{'osm_id': shop[0], 'name': (shop[1].get('name', 'NONAME').encode('utf-8')).replace("'", "`"), 'latitude': shop[2][1], 'longitude': shop[2][0]}
	# print sql
	# исполняем SQL-запрос
	cursor.execute(sql)
	# применяем изменения к базе данных
	db.commit()

# закрываем соединение с базой данных
db.close()
