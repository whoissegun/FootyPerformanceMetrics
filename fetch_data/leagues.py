from utils.utils import fetch_data

def fetch_league_by_name(leagueName):
    endpoint = "/leagues"
    params = {
        "name": leagueName
    }

    return fetch_data(endpoint, params)

