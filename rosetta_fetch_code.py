import requests
import os
import json
from bs4 import BeautifulSoup
import time


# Function to write code to a file
def write_code_to_file(folder_path, name, code):
    filename = f"{name}.txt"
    filepath = os.path.join(folder_path, filename)

    with open(filepath, "w") as file:
        file.write(code)


def main():
    # Load JSON data from file
    json_file = "tasks2.json"

    with open(json_file, "r") as file:
        data = json.load(file)

    # Create a folder to store the code files
    output_folder = "code"
    os.makedirs(output_folder, exist_ok=True)

    # Loop through each task in the JSON data
    for task, link in data.items():
        try:
            task_name = task
            task_link = "https://rosettacode.org" + link

            print(f"Fetching Code for {task_name}")

            # Send a GET request to the task link
            response = requests.get(task_link)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the HTML content
                soup = BeautifulSoup(response.content, "html.parser")

                # Find divs with mw-highlight-lang-java class
                java_divs = soup.find_all("div", class_="mw-highlight-lang-java")

                # Find divs with mw-highlight-lang-python class
                python_divs = soup.find_all("div", class_="mw-highlight-lang-python")

                # Create a folder for the current task
                task_folder = os.path.join(output_folder, task_name)
                os.makedirs(task_folder, exist_ok=True)

                # Save Java code to a file
                for i, div in enumerate(java_divs):
                    code = div.find("pre").text
                    write_code_to_file(task_folder, f"java_code_{i+1}", code)

                # Save Python code to a file
                for i, div in enumerate(python_divs):
                    code = div.find("pre").text
                    write_code_to_file(task_folder, f"python_code_{i+1}", code)

                print(f"Code saved for task: {task_name}")
            else:
                print(
                    f"Failed to retrieve the page for task: {task_name}. Status code:",
                    response.status_code,
                )
            time.sleep(0.05)
        except Exception as e:
            print(f"Exception while fetching code for {task_name}")


if __name__ == "__main__":
    main()
