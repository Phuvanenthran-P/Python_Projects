def analyze_repos(repos):
    total_stars = 0
    languages = {}

    for repo in repos:
        total_stars += repo.get("stargazers_count", 0)

        lang = repo.get("language")
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    return {
        "total_repos": len(repos),
        "total_stars": total_stars,
        "languages": languages
    }

def display_report(report):
    print("\n==== GitHub Repo Analysis ====")
    print("Total Repositories:", report["total_repos"])
    print("Total Stars:", report["total_stars"])
    print("Languages Used:")

    for lang, count in report["languages"].items():
        print(f"  {lang}: {count} repos")
