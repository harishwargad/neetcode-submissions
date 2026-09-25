import os
import requests

# Configuration
SESSION = os.getenv("LEETCODE_SESSION")
CSRF_TOKEN = os.getenv("CSRFTOKEN")
TARGET_FOLDER = "LeetCode"

os.makedirs(TARGET_FOLDER, exist_ok=True)

graphql_url = "https://leetcode.com/graphql"

headers = {
    "Cookie": f"LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN};",
    "x-csrftoken": CSRF_TOKEN,
    "Referer": "https://leetcode.com",
    "Content-Type": "application/json",
}

# GraphQL query to get recent accepted submissions
query = """
query recentAcSubmissions($limit: Int!) {
  recentAcSubmissionList(limit: $limit) {
    id
    title
    titleSlug
    timestamp
  }
}
"""

payload = {
    "query": query,
    "variables": {"limit": 20} # Fetches your last 20 accepted solutions per sync run
}

response = requests.post(graphql_url, json=payload, headers=headers)
if response.status_code != 200:
    print(f"Failed to connect to LeetCode API: {response.status_code}")
    exit(1)

data = response.json()
if "data" not in data or not data["data"].get("recentAcSubmissionList"):
    print("No recent submissions found or authentication failed.")
    exit(0)

submissions = data["data"]["recentAcSubmissionList"]

# Extension mapping based on LeetCode language names
lang_extensions = {
    "python": "py",
    "python3": "py",
    "cpp": "cpp",
    "java": "java",
    "python": "py",
    "javascript": "js",
    "typescript": "ts",
    "c": "c",
    "go": "go",
    "rust": "rs"
}

for sub in submissions:
    sub_id = sub["id"]
    title_slug = sub["titleSlug"]
    
    # Fetch details for each submission to get the actual source code
    detail_query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code
        lang {
          name
        }
      }
    }
    """
    detail_payload = {
        "query": detail_query,
        "variables": {"submissionId": int(sub_id)}
    }
    
    detail_res = requests.post(graphql_url, json=detail_payload, headers=headers)
    if detail_res.status_code == 200:
        detail_data = detail_res.json()
        details = detail_data.get("data", {}).get("submissionDetails")
        
        if details:
            code = details["code"]
            lang_name = details["lang"]["name"].lower()
            ext = lang_extensions.get(lang_name, "txt")
            
            # Create problem folder inside LeetCode/
            problem_dir = os.path.join(TARGET_FOLDER, title_slug)
            os.makedirs(problem_dir, exist_ok=True)
            
            file_path = os.path.join(problem_dir, f"solution.{ext}")
            
            # Write code to file if it doesn't already exist or has updates
            if not os.path.exists(file_path) or open(file_path, "r", encoding="utf-8").read() != code:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(code)
                print(f"Synced: {title_slug} ({lang_name})")

print("LeetCode sync completed successfully.")
