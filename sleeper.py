
import pandas as pd
from sleeper_wrapper import League


league_id = '563733789878083584'

league = League(league_id)

class MyLeague():

	def __init__(self, league):
		self.league = league

	def getNames(self):
		data = League.get_users(league)
		js = pd.json_normalize(data)

		for key, value in js.items():
			if key == 'display_name':
				print(str(value[0:]))

def getNames(league):
	data = League.get_users(league)
	js = pd.json_normalize(data)

	for key, value in js.items():
		if key == 'display_name':
			return str(value[0:])

x = getNames(league)
