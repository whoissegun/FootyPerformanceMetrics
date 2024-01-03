from fetch_data.leagues import fetch_league_by_name
from fetch_data.teams import fetch_team_by_name, fetch_team_stats_in_a_season
from fetch_data.fixtures import fetch_fixtures_ids_and_outcomes
from analyze_data import plot_win_draw_loss, plot_team_card_distribution, plot_goal_distribution, plot_fixtures_stats

def main():
    teamName = "Manchester City"
    leagueName = "Premier League"
    season = 2022
    
    leagueResponse = fetch_league_by_name(leagueName)
    leagueId = leagueResponse[0]['league']['id']
    
    teamResponse = fetch_team_by_name(teamName)
    teamId = teamResponse[0]['team']['id']
    
    teamStatsResponse = fetch_team_stats_in_a_season(leagueId, season, teamId)
    
    plot_win_draw_loss(teamStatsResponse)
    plot_team_card_distribution(teamStatsResponse)
    plot_goal_distribution(teamStatsResponse)

    fixture_ids, game_outcomes = fetch_fixtures_ids_and_outcomes(leagueId, season, teamId)
    plot_fixtures_stats(fixture_ids, game_outcomes, teamId)


    
if __name__ == "__main__":
    main()
    
	