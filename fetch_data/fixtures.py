from utils.utils import fetch_data

def fetch_fixtures_ids_and_outcomes(league, season, team):
    endpoint = "/fixtures"
    params = {
        "league": league,
        "season": season,
        "team": team
    }

    fixtures = fetch_data(endpoint, params)

    fixture_ids = []
    game_outcomes = [] # 0 for loss, 1 for draw, 2 for win
    isHome =False

    for fixture in fixtures:
        if fixture['teams']['home']['id'] == team:
            isHome = True
        else:
            isHome = False

        fixture_ids.append(fixture['fixture']['id'])
        
        if not fixture['teams']['home']['winner'] and not fixture['teams']['away']['winner']: #draw
            game_outcomes.append(1)
        
        elif (fixture['teams']['home']['winner'] == True and isHome == True) or \
            (fixture['teams']['away']['winner'] == True and isHome == False): # win
            game_outcomes.append(2)
        
        else: #loss
            game_outcomes.append(0)

    return fixture_ids, game_outcomes