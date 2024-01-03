from utils.utils import fetch_data

def fetch_team_stats_in_a_season(league, season, team):

    if(season == None or season > 2023):
        raise Exception("Invalid season")
    
    endpoint = "/teams/statistics"
    params = {
        "league": league,
        "season": season,
        "team": team
    }

    return fetch_data(endpoint, params)

def fetch_team_stats_in_lastX_seasons(league, season, team, lastX):
        
        stats = [] # list of stats for each season
        if(season == None or season > 2023):
            raise Exception("Invalid season")
        
        for i in range(0, lastX):
            stats.append(fetch_team_stats_in_a_season(league, season - i, team)) # fetch stats for each season and append to list
        

def fetch_team_by_name(teamName):
    endpoint = "/teams"
    params = {
        "name": teamName
    }

    return fetch_data(endpoint, params)