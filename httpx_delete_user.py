import httpx

from tools.fakers import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print(f"Create user data status: {create_user_response.status_code}")
print(f"Create user data: {create_user_response_data}")

login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response = httpx.post(url="http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(f"Login data: {login_response_data}")

delete_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
delete_user_response = httpx.delete(
    f"http://127.0.0.1:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=delete_user_headers
)

print(f"Delete user status code: {delete_user_response.status_code}")
