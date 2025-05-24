from bs4 import BeautifulSoup
import requests

url = 'http://www.imdb.com/search/title?release_date=' + year + ',' + year + '&title_type=feature'

# COPILOT GENERATED CODE

# Send a GET request to the URL
response = requests.get(url)    

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the movie containers
    movies = soup.find_all('div', class_='lister-item mode-advanced')

    # Loop through each movie container and extract the title and rating
    for movie in movies:
        title = movie.h3.a.text
        rating = movie.strong.text if movie.strong else 'N/A'
        print(f'Title: {title}, Rating: {rating}')

else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')




