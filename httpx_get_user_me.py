import httpx
import json


login_payload = {
    "email": "test1@gmail.com",
    "password": "123456"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(f"Status code 'login': {login_response.status_code}")
access_token = login_response_data['token']['accessToken']

users_me_response = httpx.get("http://localhost:8000/api/v1/users/me",
                              headers={"Authorization": f"Bearer {access_token}"})
user_data = users_me_response.json()
formatted_user_me_data = json.dumps(user_data, indent=4, ensure_ascii=False)

print(f"Status code 'users me': {users_me_response.status_code}")
print(formatted_user_me_data)
