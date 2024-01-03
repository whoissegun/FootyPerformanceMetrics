from dotenv import load_dotenv
import os
import requests
import matplotlib.pyplot as plt

def fetch_data(endpoint, params):
    load_dotenv()
    baseUrl = os.getenv("RAPID_API_BASE_URL")
    apiKey = os.getenv("RAPID_API_KEY")
    apiHost = os.getenv("RAPID_API_HOST")

    print(baseUrl)

    url = baseUrl + endpoint

    headers = {
	    "X-RapidAPI-Key": apiKey,
	    "X-RapidAPI-Host": apiHost
    }

    try:

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()['response']

        else:
            print(response, response.status_code)
            raise Exception("Error fetching data")
    
    except Exception as e:
        print(e)
        return None


def plot_pie_chart(labels, sizes, colours, title):
    plt.pie(sizes, labels=labels, colors=colours, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title(title)
    plt.show()

def plot_bar_chart(labels, sizes, colours, title):
    plt.bar(labels, sizes, color=colours)
    plt.title(title)
    plt.show()


def plot_stacked_bar_chart(categories, title, labels, *args):
    colours = ['yellow', 'green', 'red', 'blue', 'orange', 'purple', 'pink', 'brown', 'grey', 'black']
    
    for i, dataset in enumerate(args):
        if i == 0:
            plt.bar(categories, dataset, color=colours[i], label = labels[i])
        else:
            plt.bar(categories, dataset, bottom=args[i-1], color=colours[i], label = labels[i])

    plt.title(title)
    plt.legend()
    plt.show()

def plot_histogram(data, title, xlabel, ylabel):
    plt.hist(data, bins=range(0,120,15) , edgecolor='black', linewidth=1.2)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_scatter_plot(x, y, title, xlabel, ylabel, color, marker, label):
    plt.scatter(x, y, color=color, marker=marker, label=label)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axhline(y=1, color='gray', linestyle='--')  # For visual reference
    plt.axhline(y=2, color='gray', linestyle='--')  # For visual reference
    plt.legend()
    plt.show()