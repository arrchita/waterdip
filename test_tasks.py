import requests
import json

def test_create_task():
    print("Running test_create_task")
    r = requests.post('http://localhost:5000/v1/tasks', json={"title": "My First Task"})
    assert isinstance(r.json()["id"], int)
    assert len(r.json()) == 1
    print("test_create_task passed")

def test_list_all_tasks():
    print("Running test_list_all_tasks")
    r = requests.get('http://localhost:5000/v1/tasks')
    assert isinstance(r.json()["tasks"], list)
    assert len(r.json()) == 1
    assert isinstance(r.json()["tasks"][0]["id"], int)
    assert isinstance(r.json()["tasks"][0]["title"], str)
    assert isinstance(r.json()["tasks"][0]["is_completed"], bool)
    assert len(r.json()["tasks"][0]) == 3
    print("test_list_all_tasks passed")

def test_get_task():
    print("Running test_get_task")
    r = requests.get('http://localhost:5000/v1/tasks/1')
    print(f"Response Status Code: {r.status_code}")
    print(f"Response Content: {r.text}")  # Print the raw response content
    assert isinstance(r.json(), dict)
    assert isinstance(r.json()["id"], int)
    assert isinstance(r.json()["title"], str)
    assert isinstance(r.json()["is_completed"], bool)
    assert len(r.json()) == 3
    print("test_get_task passed")

def test_update_task():
    print("Running test_update_task")
    r = requests.put('http://localhost:5000/v1/tasks/1', json={"title": "My 1st Task", "is_completed": True})
    assert not r.content
    print("test_update_task passed")

def test_delete_task():
    print("Running test_delete_task")
    r = requests.delete('http://localhost:5000/v1/tasks/1')
    assert not r.content
    print("test_delete_task passed")

import requests
import json

def test_create_task():
    print("Running test_create_task")
    r = requests.post('http://localhost:5000/v1/tasks', json={"title": "My First Task"})
    assert isinstance(r.json()["id"], int)
    assert len(r.json()) == 1
    print("test_create_task passed")

def test_list_all_tasks():
    print("Running test_list_all_tasks")
    r = requests.get('http://localhost:5000/v1/tasks')
    assert isinstance(r.json()["tasks"], list)
    assert len(r.json()) == 1
    assert isinstance(r.json()["tasks"][0]["id"], int)
    assert isinstance(r.json()["tasks"][0]["title"], str)
    assert isinstance(r.json()["tasks"][0]["is_completed"], bool)
    assert len(r.json()["tasks"][0]) == 3
    print("test_list_all_tasks passed")

def test_get_task():
    print("Running test_get_task")
    r = requests.get('http://localhost:5000/v1/tasks/1')
    print(f"Response Status Code: {r.status_code}")
    print(f"Response Content: {r.text}")  # Print the raw response content
    assert isinstance(r.json(), dict)
    assert isinstance(r.json()["id"], int)
    assert isinstance(r.json()["title"], str)
    assert isinstance(r.json()["is_completed"], bool)
    assert len(r.json()) == 3
    print("test_get_task passed")

def test_update_task():
    print("Running test_update_task")
    r = requests.put('http://localhost:5000/v1/tasks/1', json={"title": "My 1st Task", "is_completed": True})
    assert not r.content
    print("test_update_task passed")

def test_delete_task():
    print("Running test_delete_task")
    r = requests.delete('http://localhost:5000/v1/tasks/1')
    assert not r.content
    print("test_delete_task passed")

if __name__ == "__main__":
    test_create_task()
    test_list_all_tasks()
    test_get_task()
    test_update_task()
    test_delete_task()

