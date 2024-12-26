import requests
import json

def chat_with_server(message):
  """
  Sends a message to the server and returns the response.

  Args:
      message: The message to send to the server.

  Returns:
      The server's response as a dictionary, or None if an error occurred.
  """
  try:
    url = 'http://localhost:5000/chat'  # Make sure this matches your server
    headers = {'Content-Type': 'application/json'}  # Important!
    data = {'message': message}

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

    return response.json()

  except requests.exceptions.RequestException as e:
    print(f"Error communicating with server: {e}")
    if response is not None:
      print(f"Server Response: {response.text}")  # Print server response for debugging
    return None

if __name__ == "__main__":
  user_message = 'Hello, how are you?'
  server_response = chat_with_server(user_message)

  if server_response:
    print("Server Response:")
    print(server_response['response'])

  user_message = "What is the capital of France?"
  server_response = chat_with_server(user_message)

  if server_response:
    print("Server Response:")
    print(server_response['response'])