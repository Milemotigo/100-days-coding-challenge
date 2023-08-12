import requests

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)  # Assuming the data is in JSON format, you can also use data parameter for form data
        response.raise_for_status()  # Raise an exception if the request was not successful (status code >= 400)
        return response.json()  # Assuming the server returns JSON data in the response
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

# Example usage
if __name__ == "__main__":
    api_url = "https://example.com/api/resource"
    data_to_send = {
        "username": "john_doe",
        "email": "john@example.com",
        "age": 30
    }
    result = send_post_request(api_url, data_to_send)
    if result:
        print("POST request successful. Response:")
        print(result)

