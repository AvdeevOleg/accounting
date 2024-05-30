from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import requests

def fetch_github():
    response = requests.get('https://api.github.com')
    if response.status_code == 200:
        print('GitHub API is reachable.')
    else:
        print('Failed to reach GitHub API.')

if __name__ == '__main__':
    print(f"Current date and time: {datetime.now()}")
    calculate_salary()
    get_employees()
    fetch_github()
