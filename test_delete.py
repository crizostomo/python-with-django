import requests

headers = {'Authorization': 'Token e1397716861a767d9fcdf156329993831ec42bf3'}

base_course_url = 'http://localhost:8000/api/v2/courses/'
appraisals_course_url = 'http://localhost:8000/api/v2/appraisals/'

result = requests.delete(url=f'{base_course_url}3/', headers=headers)

# Testing the status Code HTTP 204
assert result.status_code == 204
print(result.status_code)

# Testing if the returned content is equal to 0
assert len(result.text) == 0