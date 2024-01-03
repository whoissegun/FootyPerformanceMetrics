import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils.utils import plot_bar_chart, plot_stacked_bar_chart,fetch_data, plot_scatter_plot
import time

def plot_win_draw_loss(data):
    
    draws = []
    wins = []
    losses = []
    labels = ['Draws', 'Wins', 'Losses']

    draws = [data['fixtures']['draws']['home'], data['fixtures']['draws']['away']]
    wins = [data['fixtures']['wins']['home'], data['fixtures']['wins']['away']]
    losses = [data['fixtures']['loses']['home'], data['fixtures']['loses']['away']]
        
    categories = ['Home', 'Away']
    title = f'{data["team"]["name"] } win, draw, loss stats in {data["league"]["season"]}'

    plot_stacked_bar_chart(categories, title,  labels, draws, wins, losses)

def plot_team_card_distribution(data): #plot team card stats in a season
    yellow_card_count = 0
    red_card_count = 0
    yellow_card_time_distrubution = {}
    red_card_time_distrubution = {}

    for i in data['cards']['yellow'].items():

        if not i[1]["total"]:
            yellow_card_count += 0
            yellow_card_time_distrubution[i[0]] = 0
        else:
            yellow_card_count += i[1]["total"]

            yellow_card_time_distrubution[i[0]] = i[1]["total"]
    
    for i in data['cards']['red'].items():
        if not i[1]["total"]:
            red_card_count += 0
            red_card_time_distrubution[i[0]] = 0
        else:
            red_card_count += i[1]["total"]
            red_card_time_distrubution[i[0]] = i[1]["total"]


    time_distribution_labels = [i for i in yellow_card_time_distrubution] #get time distribution labels
    yellow_card_time_distribution_values = [i for i in yellow_card_time_distrubution.values()] #get time distribution values
    red_card_time_distribution_values = [i for i in red_card_time_distrubution.values()] #get time distribution values

    colours = ['yellow', 'red', 'green', 'blue', 'orange', 'purple', 'pink', 'brown', 'grey', 'black']


    yellow_and_red_card_count = [yellow_card_count, red_card_count]

    labels = 'Yellow', 'Red'

    title = f'{data["team"]["name"] } yellow and red card stats in {data["league"]["season"]}'

    plot_bar_chart(labels, yellow_and_red_card_count, colours, title)

    print(time_distribution_labels)
    print(yellow_card_time_distribution_values)

    plot_bar_chart(time_distribution_labels, yellow_card_time_distribution_values, colours, 'Yellow card time distribution')
    plot_bar_chart(time_distribution_labels, red_card_time_distribution_values, colours, 'Red card time distribution')


def plot_goal_distribution(data): #plot goal distribution stats in a season
    categories = ['0-15', '16-30', '31-45', '46-60', '61-75', '76-90', '91-105', '106-120' ]
    category2 = ['For', 'Against']
    labels = ['Home', 'Away']
    goals_for_time_distribution = []
    goals_against_time_distribution = []

    goals_for = [data['goals']['for']['total']['home'], data['goals']['for']['total']['away']]
    goals_against = [data['goals']['against']['total']['home'], data['goals']['against']['total']['away']]
    title = f'{data["team"]["name"] } goal distribution stats in {data["league"]["season"]}'

    for _,value in data['goals']['for']['minute'].items():
        if not value['total']:
            goals_for_time_distribution.append(0)
        else:
            goals_for_time_distribution.append(value['total'])
        
    for _,value in data['goals']['against']['minute'].items():
        if not value['total']:
            goals_against_time_distribution.append(0)
        else:
            goals_against_time_distribution.append(value['total'])
        
    

    print(goals_for_time_distribution)
    plot_stacked_bar_chart(category2, title, labels, goals_for, goals_against)
    
    plot_bar_chart(categories, goals_for_time_distribution, 'blue', f'Time Distribution of the goals {data["team"]["name"]} scored in {data["league"]["season"]}')
    plot_bar_chart(categories, goals_against_time_distribution, 'red', f'Time Distribution of the goals {data["team"]["name"]} conceded in {data["league"]["season"]}')
    
def plot_fixtures_stats(fixture_ids, game_outcomes, teamId):
    game_possession = [] # list of possession for each game. a parallel list to fixture_ids and game_outcomes

    for fixture_id in fixture_ids:
        endpoint = f"/fixtures/statistics"
        params = {"fixture": fixture_id}
        fixture_stats = fetch_data(endpoint, params)

        if fixture_stats == None: #end if fixture_stats is None. means we have hit rate limit
            break

        for team in fixture_stats:
            if team['team']['id'] == teamId:
                str_possession = team['statistics'][9]['value']
                game_possession.append(int(str_possession.strip('%')))

                break
        
        time.sleep(1) # sleep for 1 seconds to avoid rate limiting
    
    plot_scatter_plot(game_possession, game_outcomes, 'Possession vs Game Outcomes', 'Possession %', 'Game Outcome', 'blue', 'o', 'Fixture Outcome')


    

