import requests

headers = {'Authorization': 'Token e1397716861a767d9fcdf156329993831ec42bf3'}

base_course_url = 'http://localhost:8000/api/v2/courses/'
appraisals_course_url = 'http://localhost:8000/api/v2/appraisals/'

updated_course = {
    "title": "New Django Rest Framework",
    "url": "https://www.udemy.com/course/criando-apis-rest-com-django-rest-framework-essencial-2.0"
}

result = requests.put(url=f'{base_course_url}3/', headers=headers, data=updated_course)

#Searching the course with ID 6
#course = requests.get(url=f'{base_course_url}3/', headers=headers)
#print(course.json())

# Testing the status Code HTTP 200
assert result.status_code == 201
print(result.status_code)

# Testing if the title returned is the same as informed
assert result.json()['title'] == updated_course['title']