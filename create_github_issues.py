import sys
import json
import urllib.request
import urllib.error

REPO = "shadabsayyad99-ops/capstone-final-project-devops-"

ISSUES = [
    {
        "title": "Setting up the development environment",
        "labels": ["technical-debt"],
        "body": """### User Story
**As a** DevOps Engineer  
**I need** to set up the development environment and tooling configurations  
**So that** the team can build, lint, and test microservice features reliably.

### Details and Assumptions
* Configure setup.cfg with nosetests, coverage, flake8, and pylint settings.
* Ensure database and test runners are configured.

### Acceptance Criteria
```gherkin
Given a fresh local or container workspace
When I run nosetests and linters
Then all tests pass and coverage is reported
```"""
    },
    {
        "title": "Read an account from the service",
        "labels": ["enhancement"],
        "body": """### User Story
**As a** user / API consumer  
**I need** to read an account by its ID  
**So that** I can retrieve and view the account details.

### Details and Assumptions
* REST endpoint: GET /accounts/<id>

### Acceptance Criteria
```gherkin
Given an existing account with ID 1
When I send a GET request to /accounts/1
Then I receive a 200 OK status code with the account JSON payload
```"""
    },
    {
        "title": "List all accounts in the service",
        "labels": ["enhancement"],
        "body": """### User Story
**As a** user / API consumer  
**I need** to list all accounts  
**So that** I can view all customer accounts stored in the database.

### Details and Assumptions
* REST endpoint: GET /accounts

### Acceptance Criteria
```gherkin
Given accounts exist in the database
When I send a GET request to /accounts
Then I receive a 200 OK status code with a JSON list of all accounts
```"""
    },
    {
        "title": "Update an account in the service",
        "labels": ["enhancement"],
        "body": """### User Story
**As a** user / API consumer  
**I need** to update an existing account  
**So that** customer information stays accurate and up-to-date.

### Details and Assumptions
* REST endpoint: PUT /accounts/<id>

### Acceptance Criteria
```gherkin
Given an existing account with ID 1
When I send a PUT request with updated JSON data to /accounts/1
Then I receive a 200 OK status code with the updated account information
```"""
    },
    {
        "title": "Delete an account from the service",
        "labels": ["enhancement"],
        "body": """### User Story
**As a** user / API consumer  
**I need** to delete an account  
**So that** inactive or removed customer records can be purged.

### Details and Assumptions
* REST endpoint: DELETE /accounts/<id>

### Acceptance Criteria
```gherkin
Given an existing account with ID 1
When I send a DELETE request to /accounts/1
Then I receive a 204 No Content status code and the record is deleted
```"""
    },
    {
        "title": "Automate CI checks",
        "labels": ["technical-debt"],
        "body": """### User Story
**As a** DevOps Engineer  
**I need** to automate CI checks using GitHub Actions  
**So that** code pushed to main is automatically linted and tested.

### Acceptance Criteria
```gherkin
Given code is pushed or a PR is created on main
When the GitHub Actions workflow runs
Then flake8 and nosetests execute automatically
```"""
    },
    {
        "title": "Add security headers and CORS",
        "labels": ["enhancement"],
        "body": """### User Story
**As a** Security Engineer  
**I need** to implement secure HTTP headers and CORS policies  
**So that** the application is protected against web vulnerabilities.

### Acceptance Criteria
```gherkin
Given the microservice is running
When requests are sent to the API
Then Talisman security headers and Access-Control-Allow-Origin headers are returned
```"""
    },
    {
        "title": "Containerize application using Docker",
        "labels": ["enhancement"],
        "body": """### User Story
**As a** DevOps Engineer  
**I need** to containerize the application with Docker  
**So that** it can be deployed consistently in any environment.

### Acceptance Criteria
```gherkin
Given a Dockerfile
When docker build is executed
Then an image running as non-root user theia is created
```"""
    },
    {
        "title": "Deploy application to Kubernetes",
        "labels": ["enhancement"],
        "body": """### User Story
**As a** Cloud Architect  
**I need** to deploy the microservice to a Kubernetes cluster  
**So that** it scales and self-heals in production.

### Acceptance Criteria
```gherkin
Given Kubernetes deployment and service YAML manifests
When kubectl apply is executed
Then pods, deployment, and service are created and running
```"""
    },
    {
        "title": "Automate CD pipeline using Tekton",
        "labels": ["enhancement"],
        "body": """### User Story
**As a** DevOps Engineer  
**I need** to automate the Continuous Delivery pipeline using Tekton  
**So that** every validated change is automatically built and deployed.

### Acceptance Criteria
```gherkin
Given a Tekton pipeline configuration
When pipeline run triggers
Then tasks execute clone, lint, test, build, and deploy successfully
```"""
    }
]

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_github_issues.py <YOUR_GITHUB_TOKEN>")
        print("Or run manually via GitHub web interface following the instructions.")
        sys.exit(1)
        
    token = sys.argv[1].strip()
    url = f"https://api.github.com/repos/{REPO}/issues"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "Antigravity-DevOps-Setup",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    for item in ISSUES:
        data = json.dumps(item).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req) as resp:
                res = json.loads(resp.read().decode())
                print(f"Created Issue #{res.get('number')}: {res.get('title')}")
        except urllib.error.HTTPError as e:
            err = e.read().decode()
            print(f"Failed to create '{item['title']}': HTTP {e.code} - {err}")
        except Exception as e:
            print(f"Error creating '{item['title']}': {e}")

if __name__ == "__main__":
    main()
