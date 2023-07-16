import json
import requests
from bs4 import BeautifulSoup

# Base URL
base_url = "https://rosettacode.org"

# URL of the first page
url = "https://rosettacode.org/wiki/Category:Programming_Tasks"

tasks = {}

# Loop until there is no "next page" link
while True:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the section for "Programming Tasks"
        programming_tasks_section = soup.find("div", {"id": "mw-pages"})

        # Find all the links under the "Programming Tasks" section
        links = programming_tasks_section.find_all("a")

        # Fetch and print the text of each link
        for link in links:
            if 'wiki' in link.get('href', ''):
                tasks[link.text] = link['href']
                print(link['href'], link.text)

        # Find the "next page" link
        next_page_link = soup.find("a", text="next page")

        # Check if there is a "next page" link
        if next_page_link:
            # Update the URL to the next page
            url = base_url + next_page_link["href"]
        else:
            # No "next page" link found, break the loop
            break
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)
        break

with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)
