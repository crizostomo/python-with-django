import requests
import jsonpath

appraisals = requests.get('http://localhost:8000/api/v2/appraisals/')

results = jsonpath.jsonpath(appraisals.json(), 'results')

print(results)

first = jsonpath.jsonpath(appraisals.json(), 'results[0]')

print(first)

name = jsonpath.jsonpath(appraisals.json(), 'results[0].name')

print(name)

grade = jsonpath.jsonpath(appraisals.json(), 'results[0].appraisal')

print(grade)

names = jsonpath.jsonpath(appraisals.json(), 'results[*].name')

print(names)

grades = jsonpath.jsonpath(appraisals.json(), 'results[*].appraisal')

print(grades)