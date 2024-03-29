import validators
import subprocess
import os
from scraping_links import run_this


def main():
    url = input("Enter the scrolller URL : ")
    if validators.url(url) and url.startswith("https://scrolller.com/"):
        run_this(url)
        cwd = os.getcwd()
        python_script_path = os.path.join(cwd, "image downloader.py")
        project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        venv_python_path = os.path.join(project_directory, "venv", "Scripts", "python.exe")
        subprocess.run([venv_python_path, python_script_path])
    else:
        print("Enter a valid URL Link")


if __name__ == "__main__":
    main()
