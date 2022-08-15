import requests

headers = {'Authorization': 'Token e1397716861a767d9fcdf156329993831ec42bf3'}

base_course_url = 'http://localhost:8000/api/v2/courses/'
appraisals_course_url = 'http://localhost:8000/api/v2/appraisals/'

result = requests.get(url=base_course_url, headers=headers)

print(result.json())

# Testing if the Endpoint is correct

assert result.status_code == 200
print(result.status_code)

# Testing the records quantity

assert result.json()['count'] == 4
print(result.json()['count'] == 4)

# Testing if the title of the first course is correct

assert result.json()['results'][0]['title'] == 'Java'