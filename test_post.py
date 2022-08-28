import requests

headers = {'Authorization': 'Token e1397716861a767d9fcdf156329993831ec42bf3'}

base_course_url = 'http://localhost:8000/api/v2/courses/'
appraisals_course_url = 'http://localhost:8000/api/v2/appraisals/'

new_course = {
    "title": "Agil Management with Scrum",
    "url": "http://www.geekuniversity.com.br/scrum"
}

result = requests.post(url=base_course_url, headers=headers, data=new_course)

print(result.json())

# Testing the status Code HTTP 201
assert result.status_code == 201
print(result.status_code)

# Testing if the title returned is the same as informed
assert result.json()['title'] == new_course['title']