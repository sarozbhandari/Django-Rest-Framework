import requests

def client():
    
    data = {
            "username": "Deutsch", 
            "email": "sharroz@gmail.com",
            "password1":"Changeme123",
            "password2":"Changeme123",
            }

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
                            data=data)

    # token_h = "Token 8d78aeb571508c10cf2c226bb29c7d26d6c8aeda"
    # headers = {"Authorization": token_h}
    # response = requests.get("http://127.0.0.1:8000/api/profiles/", headers = headers)

    print("Status Code:", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()