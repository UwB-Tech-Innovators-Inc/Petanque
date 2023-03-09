from Petanque.settings import connection_string
from pymongo import MongoClient


client = MongoClient(connection_string)
db = client['Petanque']
# collection = db['players']
collection = db['base_player']

# db.players.insert_many(
#     [
#         {'first_name': 'Szymon',
#          'last_name': 'Kołodziejski',
#          'license': True
#          },
#         {'first_name': 'Remigiusz',
#          'last_name': 'Składanek',
#          'license': False
#          },
#         {'first_name': 'Cezary',
#          'last_name': 'Androsiuk',
#          'license': False
#          },
#     ]
# )

query = {'first_name': 'Cezary'}
new_values = {'$set': {'license': True}}

collection.update_one(query, new_values)

players_of_team = list(db.players.find())
print(players_of_team)

# db.teams.insert_one(
#     {'name': 'UwB',
#      'desc': 'University Team',
#      'players': {'$set': {'players': players_of_team}},
#      }
# )

print(db.players.find({}))

client.close()
