
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


def single_group_conditions(group):
    teams = {}
    for team in group["teams"]:
        team_name = group["teams"][team]
        teams[team_name] = 0  # add new    key: value

    for round_name in group["games"]:
        for game_name in group["games"][round_name]:
            game = group["games"][round_name][game_name]
            # print(game)
            if game["result_1"] > game["result_2"]:
                teams[game["team_1"]] += 1
            elif game["result_1"] < game["result_2"]:
                teams[game["team_2"]] += 1
            else:
                print("nie powinno być identycznych wyników meczu")
                exit(1)

    conflict_exits = 0
    # for team_name1 in teams:
    #     for team_name2 in teams:
    #         if team_name1 != team_name2:
    #             continue
    #         if teams[team_name1] == teams[team_name2]:
    #             print(teams[team_name1], " ", teams[team_name2], end=": ")
    #             print("konflikt!")
    #             conflict_exits = 1

    if not conflict_exits:
        # sort by the highest win values
        sorted_teams = dict(sorted(teams.items(), key=lambda x: x[1], reverse=True))

        # # return decreasing ordered dictionary with sums of wins
        # return sorted_teams

        # return names in decreasing ordered array
        array_of_team_names = []
        for team_name in sorted_teams:
            array_of_team_names.append(team_name)
        return array_of_team_names
    else:
        # there are 2 or more equal win sums
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
        array_of_team_names = single_group_conditions(group)
        print(array_of_team_names)
        print()
    #     group_result =
    #     for team in group_result:
    #         group_teams.append(team)
    #         if len(group_teams) == 3:
    #             break
    #
    #     i += 1
    #     if i == 2:
    #         all_groups.append(group_teams.copy())
    #         group_teams.clear()
    #         i = 0
    #
    # return phase_1_prepare_result_json(all_groups)
    pass

def tmp():
    # https://www.geeksforgeeks.org/read-json-file-using-python/

    file = open('petanque_mpm_faza_1.json')
    data = json.load(file)
    file.close()
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
