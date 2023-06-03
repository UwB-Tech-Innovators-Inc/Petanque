
import json

def phase_1_prepare_result_json(array):
    result = {
        "name": "faza_2",
        "group_9": {
            "teams": {
                "team_1": "",
                "team_2": "",
                "team_3": "",
                "team_4": "",
                "team_5": "",
                "team_6": ""
            },
            "games": {}
        },
        "group_10": {
            "teams": {
                "team_1": "",
                "team_2": "",
                "team_3": "",
                "team_4": "",
                "team_5": "",
                "team_6": ""
            },
            "games": {}
        },
        "group_11": {
            "teams": {
                "team_1": "",
                "team_2": "",
                "team_3": "",
                "team_4": "",
                "team_5": "",
                "team_6": ""
            },
            "games": {}
        },
        "group_12": {
            "teams": {
                "team_1": "",
                "team_2": "",
                "team_3": "",
                "team_4": "",
                "team_5": "",
                "team_6": ""
            },
            "games": {}
        }
    }

    i = 9
    while i <= 12:
        j = 1
        while j <= 6:
            result["group_" + str(i)]["teams"]["team_" + str(j)] = array[i - 9][j - 1]
            j += 1
        i += 1

    print(result)

    pass

def phase_1_single_group(group):
    teams = group["teams"]
    teams_sum = {
        teams["team_1"]: {
            "wins": 0, "balance_z": 0, "gained_z": 0, "lost_z": 0, "balance": 0, "gained": 0, "lost": 0
        },
        teams["team_2"]: {
            "wins": 0, "balance_z": 0, "gained_z": 0, "lost_z": 0, "balance": 0, "gained": 0, "lost": 0
        },
        teams["team_3"]: {
            "wins": 0, "balance_z": 0, "gained_z": 0, "lost_z": 0, "balance": 0, "gained": 0, "lost": 0
        },
        teams["team_4"]: {
            "wins": 0, "balance_z": 0, "gained_z": 0, "lost_z": 0, "balance": 0, "gained": 0, "lost": 0
        }
    }
    games = group["games"]
    for round in games:
        for game_name in games[round]:
            game = games[round][game_name]

            t_sum_1 = teams_sum[game["team_1"]]
            t_sum_2 = teams_sum[game["team_2"]]

            if game["result_1"] > game["result_2"]:
                t_sum_1["wins"] += 1
                t_sum_1["balance_z"] += game["result_1"] - game["result_2"]

                t_sum_2["wins"] += 0
                t_sum_2["balance_z"] += game["result_1"] - game["result_2"]
            else:
                t_sum_1["wins"] += 0
                t_sum_1["balance_z"] += game["result_2"] - game["result_1"]

                t_sum_2["wins"] += 1
                t_sum_2["balance_z"] += game["result_2"] - game["result_1"]

            t_sum_1["gained_z"] += game["result_1"]
            t_sum_1["lost_z"] += game["result_2"]
            t_sum_2["gained_z"] += game["result_2"]
            t_sum_2["lost_z"] += game["result_1"]

    # print(teams_sum)
    result = []
    for name in teams_sum:
        result.append(name)
    return result

    pass


def phase_1_result(json):
    if json["name"] != "faza_1":
        print("tylko dla \"faza_1\"")
        return

    i = 0
    group_teams = []
    all_groups = []
    for group_name in json:
        if group_name == "name":
            continue

        group = json[group_name]
        group_result = phase_1_single_group(group)
        for team in group_result:
            group_teams.append(team)
            if len(group_teams) == 3:
                break

        i += 1
        if i == 2:
            all_groups.append(group_teams.copy())
            group_teams.clear()
            i = 0

    return phase_1_prepare_result_json(all_groups)
    pass

def tmp():
    # https://www.geeksforgeeks.org/read-json-file-using-python/

    file = open('petanque_mpm_faza_1.json')
    data = json.load(file)
    file.close()
    print(data)
    phase_1_result(data)

    pass

    # kontakty = {
    #     "Jan": {"numer1": 111111111, "numer2": 222222222, "numer3": 333333333},
    #     "Jacek": {"numer1": 444444444, "numer2": 555555555, "numer3": 666666666},
    #     "Janusz": {"numer1": 777777777, "numer2": 888888888, "numer3": 999999999}
    # }
    #
    # print()
    # for imie in kontakty:
    #     print(imie, " ma numery telefonu", end=": ")
    #     for numer in kontakty[imie]:
    #         print(kontakty[imie][numer], end=", ")
    #     print()

tmp()
