from github_api import fetch_repos
from utils import analyze_repos, display_report

username = input("Enter GitHub username: ")

repos = fetch_repos(username)

if repos:
    report = analyze_repos(repos)
    display_report(report)
else:
    print("No repositories found or invalid username.")
