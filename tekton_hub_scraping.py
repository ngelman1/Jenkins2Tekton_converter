import requests
import time
import re

SEARCH_URL = "https://artifacthub.io/api/v1/packages/search"
DETAIL_URL = "https://artifacthub.io/api/v1/packages/{repoKind}/{repoName}/{packageName}"

def get_all_tasks():
    limit = 60
    offset = 0
    results = []

    while True:
        params = {"kind": 7, "limit": limit, "offset": offset}
        r = requests.get(SEARCH_URL, params=params)
        r.raise_for_status()
        data = r.json()
        packages = data.get("packages", [])
        if not packages:
            break

        for pkg in packages:
            repo = pkg.get("repository", {})
            repo_kind = repo.get("kind")
            repo_name = repo.get("name")
            pkg_name = pkg.get("name")
            if repo_kind == 7:
                results.append((repo_kind, repo_name, pkg_name))

        offset += limit
        time.sleep(0.1)

    return results



def fetch_task_details(repo_kind, repo_name, pkg_name):
    url = DETAIL_URL.format(repoKind=repo_kind, repoName=repo_name, packageName=pkg_name)
    r = requests.get(url)
    r.raise_for_status()
    return r.json()



def extract_section_from_readme(pkg, section_name):
    readme = pkg.get("data", {}).get("readme") or pkg.get("readme", "")
    if not readme: return None

    lines = readme.splitlines()
    content = []
    inside = False
    header_regex = re.compile(rf"^##+\s+.*{section_name}.*", re.IGNORECASE)
    next_header_regex = re.compile(r"^##+") # ^: new line, ##: subsection

    for line in lines:
        if header_regex.match(line): #beginig
            inside = True
            continue
        if inside and next_header_regex.match(line): #end
            break
        if inside:
            content.append(line)

    result = "\n".join(content).strip()
    return result if result else None


def get_source_code_link(pkg) -> str:
    links = pkg.get('links', [])
    for link in links:
        url = link.get('url', '')
        if url and url.endswith(".yaml"):
            return f" - {link.get('name')}: {url}"
    return "No source code link was found"


def main():
    tasks = get_all_tasks()
    print(f"\nFound {len(tasks)} Tekton tasks.\n")

    for repo_kind, repo_name, pkg_name in tasks:
        print("=" * 80)
        print(f"Task: {pkg_name} (repo: {repo_name})")
        print("-" * 80)

        try:
            pkg = fetch_task_details(repo_kind, repo_name, pkg_name)
        except Exception as e:
            print(f"Failed fetching: {e}")
            continue

        params = extract_section_from_readme(pkg, "Parameters")
        usage = extract_section_from_readme(pkg, "Usage")

        print("\nParameters:")
        print(params if params else "  None")
        print("\n")

        print("\nUsage:")
        print(usage if usage else "  None")
        print("\n")

        print("\nSource code url:")
        print(get_source_code_link(pkg))
        print("\n")

        time.sleep(0.1)


if __name__ == "__main__":
    main()
