from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:1234@cluster0.tettcne.mongodb.net/?retryWrites=true&w=majority")

db = client['Petanque']

collection = db['players']

db.players.insert_many(
    [
        {'first_name': 'Szymon',
         'last_name': 'Kołodziejski',
         'license': True
         },
        {'first_name': 'Remigiusz',
         'last_name': 'Składanek',
         'license': False
         },
        {'first_name': 'Cezary',
         'last_name': 'Androsiuk',
         'license': False
         },
    ]
)

query = {'first_name': 'Cezary'}
new_values = {'$set': {'license': True}}

collection.update_one(query, new_values)

players_of_team = list(db.players.find())
print(players_of_team)

db.teams.insert_one(
    {'name': 'UwB',
     'desc': 'University Team',
     'players': {'$set': {'players': players_of_team}},
     }
)

print(db.players.find({}))

client.close()
