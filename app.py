from flask import Flask, render_template, request
import sqlite3
import random

# Import external modules
import Gcaptcha
import MockData
import os

app = Flask(__name__)

# Function to initialize the database
def create_database():
    conn = sqlite3.connect("ovs.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vote (
        epicno TEXT NOT NULL PRIMARY KEY,
        candidate TEXT NOT NULL,
        vote TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Call the function to ensure the database is created at startup
create_database()

elist = []

# Function to save CAPTCHA text
def save_captcha_to_file(captcha_text):
    with open("captcha.txt", "w") as file:
        file.write(captcha_text)

# Function to retrieve CAPTCHA text
def get_captcha_from_file():
    with open("captcha.txt", "r") as file:
        return file.read().strip()
        
def get_vote_data():
    """ Reads vote data from Data.txt and returns it as a dictionary. """
    votes = {}
    try:
        with open("Data.txt", "r") as file:
            for line in file:
                parts = line.strip().split(": ")
                if len(parts) == 2:
                    name, count = parts[0], int(parts[1].split()[0])
                    votes[name] = count
    except FileNotFoundError:
        votes = None  # No vote data available
    return votes


@app.route('/OnlineVotingSystem')
def index():
    return render_template("index.html")

@app.route('/OnlineVotingSystem/login')
def login():
    captcha_text = Gcaptcha.generate_captcha()
    save_captcha_to_file(captcha_text)
    return render_template("login.html")

@app.route('/OnlineVotingSystem/login/vote', methods=['POST', 'GET'])
def verify():
    if request.method == 'POST':
        epicno = request.form.get('epicno')
        captch = request.form.get('captcha')
        captcha_text = get_captcha_from_file()

        print(f"\nEntered EPIC Number: {epicno}")
        print(f"Entered Captcha: {captch}")
        print(f"Real EPIC Number Status: {MockData.is_valid_epic_number(epicno)}")
        print(f"Real Captcha Data: {captcha_text}\n")

        if not MockData.is_valid_epic_number(epicno):
            return f"<p>{MockData.FalseE}</p>"

        if captcha_text != captch:
            return f"<p>{Gcaptcha.FalseC}</p>"

        # Check if the voter already voted
        conn = sqlite3.connect("ovs.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vote WHERE epicno = ?", (epicno,))
        row = cursor.fetchone()
        conn.close()

        if row:
            print(f"Epicno '{epicno}' already exists in the database.")
            return render_template("submited.html")

        mock_voter_details = MockData.get_mock_voter_details(epicno)

        elist.append(epicno)
        voter_data = {
            "vi": mock_voter_details['voter_id'],
            "nm": mock_voter_details['name'],
            "gn": mock_voter_details['gender'],
            "ag": random.randint(18, 24),
            "mo": "+91" + mock_voter_details['mobile'],
            "st": mock_voter_details['state'],
            "ad": mock_voter_details['address'],
            "co": mock_voter_details['country']
        }

        print(f"\nVoter Data: {voter_data}\n")

        return render_template("vote.html", **voter_data)

# Function to insert vote into the database
def insert_vote(epicno, candidate):
    if not elist:
        return render_template("submited.html")

    conn = sqlite3.connect("ovs.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vote (epicno, candidate, vote) VALUES (?, ?, ?)", (elist[0], candidate, "1"))
    conn.commit()
    conn.close()

    print(f"Record inserted successfully: EPICNO: {elist[0]}, Candidate: {candidate}")
    
    elist.clear()
    return render_template('submit.html')

@app.route('/c1', methods=['POST', 'GET'])
def candidate1():
    return insert_vote(elist[0], "VELUCHAMY P")

@app.route('/c2', methods=['POST', 'GET'])
def candidate2():
    return insert_vote(elist[0], "AISHA GUPTA A")

@app.route('/c3', methods=['POST', 'GET'])
def candidate3():
    return insert_vote(elist[0], "ARJUN SHARMA S")

@app.route('/c4', methods=['POST', 'GET'])
def candidate4():
    return insert_vote(elist[0], "ANANYA SINGH A")

@app.route('/c5', methods=['POST', 'GET'])
def candidate5():
    return insert_vote(elist[0], "ADITYA G")

@app.route('/c6', methods=['POST', 'GET'])
def candidate6():
    return insert_vote(elist[0], "MEERA REDDY M")

@app.route('/nota', methods=['POST', 'GET'])
def nota():
    return insert_vote(elist[0], "NOTA")
    
@app.route("/vote_data")
def display_vote_data():
    os.system("python Getvote.py")  # Run the voting script
    votes = get_vote_data()
    return render_template("vote_data.html", votes=votes)

@app.route("/result")
def display_results():
    os.system("python Getvote.py")  # Run the voting script
    votes = get_vote_data()
    
    if votes:
        winner = max(votes, key=votes.get)
        result = {"winner": winner, "votes": votes[winner]}
    else:
        result = {"winner": None, "votes": 0}

    return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
   

