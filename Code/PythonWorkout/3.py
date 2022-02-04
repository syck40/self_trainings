import random
import pathlib
import json
import requests
import yaml

def read_file():
    num = random.randint(1,20)
    while True:
        inpu = int(input('guess a number: '))
        if inpu > num:
            print('too high')
        elif inpu < num:
            print('too low')
        else:
            print(f'Just right, {num}')
            break

def parse_file():
    p = pathlib.Path('Code/PythonWorkout/text')
    print(p.anchor)
    with open(p, encoding="UTF-8") as f:
        for l in f:
            print(l)

def read_j():
    p = pathlib.Path('Code/PythonWorkout/test.json')
    p2 = pathlib.Path('Code/PythonWorkout/test.yaml')
    with p.open() as f:
        #print(json.load(f))
        print(f)
        ab = json.loads(f.read())
    
    with p2.open('w') as f:
        yaml.dump(ab, f)

def req_j():
    r = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(r.text)
    ten = [t for t in todos if t['id'] < 5]
    with open(pathlib.Path('Code/PythonWorkout/text2.json'), mode="w", encoding="UTF-8") as f:
        json.dump(ten, f, indent=4)

read_j()
