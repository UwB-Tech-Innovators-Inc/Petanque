
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


# def check_conflicts(teans):
#     ################################################## ASSUME THAT THERE ARE ONLY ONE CONFLICT ####################
#     # count number of winns
#     print(teams)
#     winsCount = {}
#     for team_name in teams:
#         if team[team_name] in winsCount:
#             winsCount[team[team_name]] += 1
#         else:
#             winsCount[team[team_name]] = 1
#
#     conflict = 0
#     additional_match = 0
#
#     # check if group have equal wins count
#     for i in winsCount:
#         if winsCount[i] == 2:
#             additional_match += 1
#     if additional_match > 1:
#         print("są 2 drużyny posiadające identyczną ilość wygranych: ", additional_match)
#         return 2
#
#     for i in winsCount:
#         if winsCount[i] >= 3:
#             conflict += 1
#     if winsCount > 1:
#         print("są ponad 3 drużyny posiadające identyczną ilość wygranych: ", winsCount)
#         return 3
#
#     return 0


def sort_by_wins_count(teams):
    sorted_teams = [[]]
    for i in range(len(teams)):
        sorted_teams.append([])
        for team_name in teams:
            if teams[team_name] == i:
                sorted_teams[i].append(team_name)
    return sorted_teams

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


    if 'G_1_1' in teams:
        teams['G_1_1'] = 2

    teams_sorted_by_values = sort_by_wins_count(teams)

    for i in teams_sorted_by_values:
        if len(i) == 2:
            print("do obsłużenia gdy 2 drużyny mają identyczną sumę zwycięstw")
            print(i)
        if len(i) >= 3:
            # function (i, array)
            print(i)


    return 1
    # conflict = check_conflicts(teams)
    #
    # if conflict == 0:
    #     # sort by the highest win values
    #     sorted_teams = dict(sorted(teams.items(), key=lambda x: x[1], reverse=True))
    #
    #     # # return decreasing ordered dictionary with sums of wins
    #     # return sorted_teams
    #
    #     # return names in decreasing ordered array
    #     array_of_team_names = []
    #     for team_name in sorted_teams:
    #         array_of_team_names.append(team_name)
    #     return array_of_team_names
    # elif conflict == 2:
    #     # there are 2 equal win sums
    #     pass
    # elif conflict == 3:
    #     # there are more than 2 equal win sums
    #     pass


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
        # print(array_of_team_names)
        # print()
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

    # pass
    #
    # d = {'G_7_1': 3, 'G_7_2': 2, 'G_7_3': 1, 'G_7_4': 0, 'G_7_x': 2}
    # a = {}
    # print(d)
    # for d_name in d:
    #     if d[d_name] in a:
    #         a[d[d_name]] += 1
    #     else:
    #         a[d[d_name]] = 1
    #     print(d[d_name], a)
    #
    # # a[3] = 4
    # print(a)

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
