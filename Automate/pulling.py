import requests
import json

# make a GET request
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

# checkif the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print the JSON result
    print(json.dumps(data, indent=4))
else:
    print(f"Failed to retrieve data: {response.status_code}")

# Script with error handling
# import requests

# Define the URL
# url = "https://jsonplaceholder.typicode.com/todos/1"

# try:
#     # Send a GET request to the URL
#     response = requests.get(url)
    
#     # Check if the response status code is OK (200)
#     if response.status_code == 200:
#         try:
#             # Attempt to parse the response as JSON
#             data = response.json()
#             print(data)
#         except requests.exceptions.JSONDecodeError:
#             print("Error: Unable to decode the response as JSON.")
#     else:
#         print(f"Error: Received response with status code {response.status_code}")
# except requests.exceptions.RequestException as e:
#     # Handle any exceptions raised during the request
#     print(f"Error: A request exception occurred - {e}")
