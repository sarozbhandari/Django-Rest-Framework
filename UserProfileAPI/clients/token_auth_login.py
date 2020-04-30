import requests

def client():
    token_h = "Token 54a6bbb41c1a15c28dcf1576bc407e87893c70af"
    # credentials = {"username": "ragnar", "password":"ragnar"}
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
    #                         data=credentials)

    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers = headers)

    print("Status Code:", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()