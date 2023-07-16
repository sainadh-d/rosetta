import os
import json


# Function to read code from a file
def read_code_from_file(file_path):
    with open(file_path, "r") as file:
        code = file.read()
    return code


# Function to generate a Markdown file for a task
def generate_markdown_file(task_name, task_link, java_code_files, python_code_files):
    markdown = f"# {task_name}\n\n"

    markdown += "## Task Link\n"
    markdown += f"[Rosetta Code - {task_name}]({task_link})\n\n"

    markdown += "## Java Code\n"
    for java_file in java_code_files:
        java_code = read_code_from_file(java_file)
        markdown += f"### {os.path.basename(java_file)}\n"
        markdown += "```java\n"
        markdown += java_code
        markdown += "\n```\n\n"

    markdown += "## Python Code\n"
    for python_file in python_code_files:
        python_code = read_code_from_file(python_file)
        markdown += f"### {os.path.basename(python_file)}\n"
        markdown += "```python\n"
        markdown += python_code
        markdown += "\n```\n\n"

    return markdown


def main():
    # Load JSON data from file
    json_file = "tasks.json"

    with open(json_file, "r") as file:
        data = json.load(file)

    # Loop through each task in the JSON data
    for task, link in data.items():
        task_name = task
        task_link = "https://rosettacode.org" + link

        # Determine the task folder path
        task_folder = os.path.join("code", task_name)

        # Collect Java code files within the task folder
        java_code_files = []
        for file_name in os.listdir(task_folder):
            if file_name.startswith("java_code"):
                java_code_files.append(file_name)

        java_code_files.sort()
        java_code_file_paths = [
            os.path.join(task_folder, file_name) for file_name in java_code_files
        ]

        # Collect Python code files within the task folder
        python_code_files = []
        for file_name in os.listdir(task_folder):
            if file_name.startswith("python_code"):
                python_code_files.append(file_name)

        python_code_files.sort()
        python_code_file_paths = [
            os.path.join(task_folder, file_name) for file_name in python_code_files
        ]

        # Generate the Markdown content
        markdown_content = generate_markdown_file(
            task_name, task_link, java_code_file_paths, python_code_file_paths
        )

        # Generate the Markdown file
        markdown_file = f"markdown/{task_name.replace('/', '')}.md"

        with open(markdown_file, "w") as file:
            file.write(markdown_content)

        print(f"Markdown file generated for task: {task_name}")

    print("All Markdown files generated successfully.")


if __name__ == "__main__":
    main()
