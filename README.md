
# Online Voting System

## Overview

The **Online Voting System** is a web-based application designed to allow students to securely cast their votes and view election results online. The system provides a simple and transparent digital voting platform where users can log in using a unique ID, verify their identity through CAPTCHA verification, and vote for their preferred candidate or select **NOTA (None of the Above)**.

![My Screenshot](./Screenshot%2026-03-08%20111816.png)




This project is built using **Python Flask as the backend** and **HTML/CSS for the frontend** to provide a lightweight and efficient voting platform.

---

## Features

* Secure **student login using unique ID**
* **CAPTCHA verification** to prevent automated voting
* Vote for **multiple candidates**
* Option to select **NOTA (None of the Above)**
* **One vote per user** restriction
* View **live election results**
* Online **voting data management**
* Simple and responsive user interface

---

## Tech Stack

**Backend**

* Python
* Flask

**Frontend**

* HTML
* CSS

**Other**

* CAPTCHA verification
* Web-based database storage (for voting records)

---

## System Workflow

1. Student logs in using a **unique ID**.
2. The system verifies the user through **CAPTCHA authentication**.
3. The student selects a **candidate or NOTA**.
4. The vote is securely stored in the system database.
5. Users can **view voting results** once voting is completed.

---

## Project Structure

```
Online-Voting-System
│
├── app.py
├── templates
│   ├── login.html
│   ├── vote.html
│   ├── result.html
│
├── static
│   ├── style.css
│
└── database
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Abineshabee/online-voting-system.git
```

### Navigate to the project folder

```bash
cd online-voting-system
```

### Install dependencies

```bash
pip install flask
```

### Run the application

```bash
python app.py
```

### Open in browser

```
http://127.0.0.1:5000
```

---

## Use Cases

* College elections
* Student council voting
* Small organization polls
* Demonstration of secure voting systems

---

## Future Improvements

* Add **database integration (MySQL/PostgreSQL)**
* Implement **blockchain-based vote verification**
* Add **admin dashboard**
* Improve **security and authentication**
* Add **real-time vote analytics**

---

## Author

Developed by **Abinesh N**

---

## License

This project is open-source and available for Educational purposes.
