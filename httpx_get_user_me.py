import httpx
import json

with httpx.Client() as client:
    login_payload = {
        "email": "test1@gmail.com",
        "password": "123456"
    }

    login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

    if login_response.status_code == 200:
        access_token = login_response.json()['token']['accessToken']
        print(f"Status code 'login': {login_response.status_code}")
    else:
        print("Ошибка при входе:", login_response.status_code, login_response.text)

    users_me_response = httpx.get("http://localhost:8000/api/v1/users/me",
                                  headers={"Authorization": f"Bearer {access_token}"})

    if users_me_response.status_code == 200:
        user_data = users_me_response.json()
        formatted_user_me_data = json.dumps(user_data, indent=4, ensure_ascii=False)
        print(f"Status code 'users me': {users_me_response.status_code}")
        print(formatted_user_me_data)
    else:
        print("Ошибка при получении данных пользователя:", users_me_response.status_code, users_me_response.text)