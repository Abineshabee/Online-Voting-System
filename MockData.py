import requests
import json
import os
import re

TrueE = "Valid EPIC Number : Congratulations! Your EPIC Number has been successfully verified. You may proceed with the intended action."

FalseE = "Invalid EPIC Number: Sorry, the EPIC Number you entered is invalid. Please try again with the correct characters to proceed."

def is_valid_epic_number(epic_number):
    # Regex to check valid EPIC Number
    regex = "^[A-Z]{3}[0-9]{7}$"

    # Compile the ReGex
    pattern = re.compile(regex)

    # If the string is empty, return false
    if epic_number is None:
        return False

    # Return if the string matched the ReGex
    return bool(re.search(pattern, epic_number))

def get_mock_voter_details(voter_id):
    data_file = "mock_voter_data.json"

    # Check if the data file exists and load the existing data
    if os.path.isfile(data_file):
        with open(data_file, "r") as f:
            mock_voter_data = json.load(f)
    else:
        mock_voter_data = {}

    # If the data doesn't exist for the given voter_id, fetch new data from the API
    if voter_id not in mock_voter_data:
        api_url = "https://randomuser.me/api/?nat=in"

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            user_data = response.json()["results"][0]

            mock_voter_details = {
                "voter_id": voter_id,
                "name": f"{user_data['name']['title']} {user_data['name']['first']} {user_data['name']['last']}",
                "gender": user_data["gender"],
                "age": user_data["dob"]["age"],
                "address": f"{user_data['location']['street']['number']} {user_data['location']['street']['name']}, {user_data['location']['city']}, {user_data['location']['state']}, {user_data['location']['postcode']}",
                "mobile": user_data["cell"],
                "state": user_data["location"]["state"],
                "country": user_data["location"]["country"]
            }

            # Store the new data in the file
            mock_voter_data[voter_id] = mock_voter_details
            with open(data_file, "w") as f:
                json.dump(mock_voter_data, f)

            return mock_voter_details
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
    else :

        return mock_voter_data[voter_id]


            

