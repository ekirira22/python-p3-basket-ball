def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }


def num_points_per_game(name):
    for teams in game_dict():
        for detail in game_dict()[teams]:
            for i in range(len(game_dict()[teams][detail])):
                if isinstance(game_dict()[teams][detail][i], dict):
                    if game_dict()[teams][detail][i]['name'] == name:
                        return game_dict()[teams][detail][i]['points_per_game']


# print(num_points_per_game('Bradley Beal'))


def player_age(name):
    for teams in game_dict():
        for detail in game_dict()[teams]:
            for i in range(len(game_dict()[teams][detail])):
                if isinstance(game_dict()[teams][detail][i], dict):
                    if game_dict()[teams][detail][i]['name'] == name:
                        return game_dict()[teams][detail][i]['age']


# print(player_age('Jarrett Allen'))


def team_colors(team_name):
    for teams in game_dict():
        if game_dict()[teams]['team_name'] == team_name:
            return game_dict()[teams]['colors']


# print(team_colors('Washington Wizards'))


def team_names():
    team_list = []
    for teams in game_dict():
        for key, val in game_dict()[teams].items():
            if key == 'team_name':
                team_list.append(val)
    return team_list


# print(team_names())

def player_numbers(team_name):
    # returns a list of the jersey numbers
    jersey_numbers = []
    for teams in game_dict():
        for key, val in game_dict()[teams].items():
            if game_dict()[teams][key] == team_name:
                for detail in game_dict()[teams]['players']:
                    jersey_numbers.append(detail['number'])

    return jersey_numbers


# print(player_numbers('Washington Wizards'))

def player_stats(name):
    # Returns a dictionary
    for teams in game_dict():
        for key, val in game_dict()[teams].items():
            if key == 'players':
                for i in range(len(game_dict()[teams][key])):
                    if game_dict()[teams][key][i]['name'] == name:
                        return game_dict()[teams][key][i]


# print(player_stats('Jarrett Allen'))

# Advanced Deliverables
def average_rebounds_by_shoe_brand():
    # Pseudocode
    # 1. Create a dictionary that will keep track of shoe brands along with their rebounds
    #   of all players that wear that particular shoe.
    # 2. As we iterate through, if brand exists, add update the new value, if it doesn't add
    #   brand as a new key
    # 3. Once we have the values, iterate through the dictionary and calculate average rebounds for
    #   each shoe brand. Use helper function find_average() and print out the result
    shoe_rebounds = dict()
    for teams in game_dict():
        for key, val in game_dict()[teams].items():
            if key == 'players':
                for i in range(len(game_dict()[teams][key])):
                    # If key (shoe_brand) does not exist, add it to the dictionary
                    if shoe_rebounds.get(game_dict()[teams][key][i]['shoe_brand']) is None:
                        shoe_rebounds.update({game_dict()[teams][key][i]['shoe_brand']: []})
                    # The above will add all keys, then append the values to the list
                    (shoe_rebounds[game_dict()[teams][key][i]['shoe_brand']]
                     .append(game_dict()[teams][key][i]['rebounds_per_game']))

    # Calculate average
    find_average(shoe_rebounds)


def find_average(shoes):

    for key, val in shoes.items():
        avg = sum(shoes[key]) / len(shoes[key])
        print(f"{key}:  {avg:.2f}")


print(average_rebounds_by_shoe_brand())

# Additional Practice

# Player with most career points
def most_career_points():
    career_list = dict()
    career_points = []
    for teams in game_dict():
        for key, val in game_dict()[teams].items():
            if key == 'players':
                for i in range(len(game_dict()[teams][key])):
                    # Create a dict to store players as keys and career points as values
                    career_list.update({game_dict()[teams][key][i]['name']: game_dict()[teams][key][i]['career_points']})
                    # Create a list for career points that we will use to get max and compare
                    career_points.append(game_dict()[teams][key][i]['career_points'])
    # Check for the largest figure, return that value

    for key, val in career_list.items():
        if val == max(career_points):
            return key


# print(most_career_points())

