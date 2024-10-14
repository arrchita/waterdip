import requests

def test_create_task():
    r = requests.post('http://localhost:5000/v1/tasks', json={"title": "My First Task"})
    assert r.status_code == 201, f"Failed with response: {r.text}"
    assert isinstance(r.json()["id"], int)

def test_list_all_tasks():
    r = requests.get('http://localhost:5000/v1/tasks')
    assert r.status_code == 200, f"Failed with response: {r.text}"
    assert isinstance(r.json()["tasks"], list)

if __name__ == "__main__":
    test_create_task()
    test_list_all_tasks()
    print("All tests passed!")
