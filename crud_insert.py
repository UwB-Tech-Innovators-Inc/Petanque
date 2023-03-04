from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:1234@cluster0.tettcne.mongodb.net/?retryWrites=true&w=majority")

db = client.Petanque

db.players.update_many(
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

players_of_team = list(db.players.find())
print(players_of_team)

db.teams.update_one(
    {'name': 'UwB',
     'desc': 'University Team',
     'players': {'$set': {'players': players_of_team}},
     }
)

print(db.players.find({}))

client.close()
