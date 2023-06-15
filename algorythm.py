
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


def solve_group_conflict_3(intrested_teams, group_games):
    # check which team was better in those who are in conflict
    print(intrested_teams)
    print(group_games)
    conflict_solved_array = []

    wins_with_intrested_teams = {}
    balance_with_intrested_teams = {}
    gained_small_points_with_intrested_teams = {}
    lost_small_points_with_intrested_teams = {}

    balance_with_all_teams = {}
    gained_small_points_with_all_teams = {}
    lost_small_points_with_all_teams = {}

    # init dicts
    for team in intrested_teams:
        wins_with_intrested_teams[team] = 0
        balance_with_intrested_teams[team] = 0
        gained_small_points_with_intrested_teams[team] = 0
        lost_small_points_with_intrested_teams[team] = 0

        balance_with_all_teams[team] = 0
        gained_small_points_with_all_teams[team] = 0
        lost_small_points_with_all_teams[team] = 0


    for round_name in group_games:
        round = group_games[round_name]
        for game_name in round:
            game = round[game_name]

            # intrested teams actions
            if game['team_1'] in intrested_teams and game['team_2'] in intrested_teams:

                # count wins with intrested teams
                if game["result_1"] > game["result_2"]:
                    wins_with_intrested_teams[game["team_1"]] += 1
                elif game["result_1"] < game["result_2"]:
                    wins_with_intrested_teams[game["team_2"]] += 1
                else:
                    print("nie powinno być identycznych wyników meczu")
                    exit(1)

                # count balance with intrested teams
                balance_with_intrested_teams[game['team_1']] += game['result_1'] - game['result_2']
                balance_with_intrested_teams[game['team_2']] += game['result_2'] - game['result_1']

                # count gained small points with intrested teams
                gained_small_points_with_intrested_teams[game['team_1']] += game['result_1']
                gained_small_points_with_intrested_teams[game['team_2']] += game['result_2']

                # count lost small points with intested teams
                lost_small_points_with_intrested_teams[game['team_1']] += game['result_2']
                lost_small_points_with_intrested_teams[game['team_2']] += game['result_1']

            # not intrested teams actions
            if game['team_1'] in intrested_teams:

                # balance with all teams
                balance_with_all_teams[game['team_1']] += game['result_1'] - game['result_2']

                # gained small points with all teams
                gained_small_points_with_all_teams[game['team_1']] += game['result_1']

                # lost small points with all teams
                lost_small_points_with_all_teams[game['team_1']] += game['result_2']

                pass
            if game['team_2'] in intrested_teams:

                # balance with all teams
                balance_with_all_teams[game['team_2']] += game['result_2'] - game['result_1']

                # gained small points with all teams
                gained_small_points_with_all_teams[game['team_2']] += game['result_2']

                # lost small points with all teams
                lost_small_points_with_all_teams[game['team_2']] += game['result_1']

                pass

    # mając 3 drużyny, dwie z nich będą miały identyczny wynik a trzecia inny i mamy ją wtedy odłączyć od drużyn zainteresowanych to muszę rozbić tego fora wyżej na wiele mniejszych

    print()
    print(wins_with_intrested_teams)
    print(balance_with_intrested_teams)
    print(gained_small_points_with_intrested_teams)
    print(lost_small_points_with_intrested_teams)
    print()
    print(balance_with_all_teams)
    print(gained_small_points_with_all_teams)
    print(lost_small_points_with_all_teams)
    print()



    # for team in intrested_teams:
    #     # count how many times each team won with others in this array


    # for round_name in group_games:
    #     round = group_games[round_name]
    #     for game_name in round:
    #         game = round[game_name]
    #
    #         print(game)
    #         pass

    for i in intrested_teams:
        conflict_solved_array.append(i)

    return conflict_solved_array

def solve_group_conflict_2(both_teams, group_games):
    # check which team won in their match
    conflict_solved_array = []
    for round_name in group_games:
        round = group_games[round_name]
        for game_name in round:
            game = round[game_name]
            if game["team_1"] == both_teams[0] and game["team_2"] == both_teams[1] or \
                game["team_1"] == both_teams[1] and game["team_2"] == both_teams[0]:

                if game["result_1"] > game["result_2"]:
                    conflict_solved_array.append(game["team_1"])
                    conflict_solved_array.append(game["team_2"])
                    break
                elif game["result_1"] < game["result_2"]:
                    conflict_solved_array.append(game["team_2"])
                    conflict_solved_array.append(game["team_1"])
                    break
                else:
                    print("nie powinno być identycznych wyników meczu")
                    exit(1)
    return conflict_solved_array



def group_by_win_count(teams):
    sorted_teams = [[]]
    for i in range(len(teams)):
        sorted_teams.append([])
        for team_name in teams:
            if teams[team_name] == i:
                sorted_teams[i].append(team_name)
    sorted_teams.reverse()
    return sorted_teams

def single_group_order(group):
    teams = {}
    # build all teams array
    for team in group["teams"]:
        team_name = group["teams"][team]
        teams[team_name] = 0  # add new    key: value

    games = group["games"]
    for round_name in games:
        round = games[round_name]
        for game_name in round:
            game = round[game_name]

            # check which team won the match and add to win counter: (dict in teams)
            if game["result_1"] > game["result_2"]:
                teams[game["team_1"]] += 1
            elif game["result_1"] < game["result_2"]:
                teams[game["team_2"]] += 1
            else:
                print("nie powinno być identycznych wyników meczu")
                exit(1)

    # # testing what happens if someone have equals wins count
    # if 'G_1_1' in teams:
    #     teams['G_1_1'] = 1
    # if 'G_1_2' in teams:
    #     teams['G_1_2'] = 1

    print(teams)

    teams_sorted_by_win_count = group_by_win_count(teams) #  [[x win], [x-1 win], ..., [1 win], [0 win]]

    teams_sorted = []
    # solve conflicts
    for teams_array in teams_sorted_by_win_count:
        if len(teams_array) == 2:
            conflict_solved_team_array = solve_group_conflict_2(teams_array, games)
            for team in conflict_solved_team_array:
                teams_sorted.append(team)

        elif len(teams_array) >= 3:
            conflict_solved_team_array = solve_group_conflict_3(teams_array, games)
            for team in conflict_solved_team_array:
                teams_sorted.append(team)

        elif len(teams_array) != 0:
            teams_sorted.append(teams_array[0])

    return teams_sorted



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
        array_of_team_names = single_group_order(group)
        print(array_of_team_names)
        break # to iterate over one group

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

    file = open('petanque_mpm_faza_1_real.json')
    data = json.load(file)
    file.close()
    phase_1_result(data)

tmp()
