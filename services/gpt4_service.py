import requests

def get_openai_response(prompt):
    # Set up the headers for the request
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_OPENAI_API_KEY,  # Use the API key from environment variable
    }

    # Prepare the payload with the prompt
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,  # Adjust as needed
    }

    # Send the request to the Azure OpenAI endpoint
    response = requests.post(AZURE_OPENAI_ENDPOINT, headers=headers, json=payload)

    # Check for successful response
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

# Example usage
if __name__ == "__main__":
    user_prompt = "What is the capital of France?"
    response = get_openai_response(user_prompt)
    print(response)  # Print the response from Azure OpenAI
