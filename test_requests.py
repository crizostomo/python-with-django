import requests

# GET Appraisals

appraisals = requests.get('http://localhost:8000/api/v2/appraisals/')

print(appraisals.status_code)

print(appraisals.json())
print(type(appraisals.json()))

#Acessing the quantity of registries
print(appraisals.json()['count'])

#Acessing the next result page
print(appraisals.json()['next'])

#Acessing the results page
print(appraisals.json()['results'])
print(type(appraisals.json()['results']))

#Acessing the first element page
print(appraisals.json()['results'][0])

#Acessing the last element page
print(appraisals.json()['results'][-1])

#Acessing the person's name that made the last appraisal
print(appraisals.json()['results'][-1]['name'])

# GET Appraisal

appraisal = requests.get('http://localhost:8000/api/v2/appraisals/1/')

print(appraisal.json())

#GET Courses

headers = {'Authorization': 'Token e1397716861a767d9fcdf156329993831ec42bf3'}

courses = requests.get(url='http://localhost:8000/api/v2/courses/', headers=headers)

print(courses.status_code)
print(courses.json())

