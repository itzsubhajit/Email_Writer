# MailCraft AI – Professional Email & Subject Writer

MailCraft AI is an AI-powered web application that helps users create professional email subject lines and email bodies from simple instructions.

The application uses **Flask** for the backend, **Groq API** for AI-powered content generation, and **HTML/CSS** for the user interface.

---

## Features

- Generate professional email subject lines
- Generate complete email bodies
- Customize email tone
- Choose email length
- Add important points and details
- Copy generated subject line
- Copy generated email body
- Clean and professional interface
- Responsive design
- AI-powered content generation
- Error handling for API failures

---

## Technology Used

- **Python**
- **Flask**
- **Groq API**
- **Requests**
- **HTML5**
- **CSS3**
- **JavaScript**

---

## Project Structure

```text
Email_Writer/
│
├── app.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```
How the Application Works
```text
User Input
     ↓
Flask Web Application
     ↓
Email Requirements
     ↓
Groq API
     ↓
AI Processing
     ↓
Professional Subject + Email Body
     ↓
Copy and Use
```
Input Fields
Recipient

Enter the person, organization, or department receiving the email.

Example:

HR Manager
Email Purpose

Describe the reason for writing the email.

Example:

I want to request leave for three days because of a family function.
Important Points

Add any specific information that should be included.

Example:
```text
Leave required from 5th October to 7th October.
I will complete all pending assignments.
I will attend classes regularly after returning.
```
Tone

The application supports different tones:

Professional
Formal
Friendly
Polite
Persuasive
Length

The user can select:

Short
Medium
Detailed
Installation
Step 1 – Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL
Step 2 – Open the Project
cd Email_Writer
Step 3 – Install Dependencies
pip install flask requests
Groq API Setup

Create your API key using Groq.

Open app.py and find:

api_key = "YOUR_GROQ_API_KEY"

Replace the placeholder with your API key.

Example:

api_key = "gsk_xxxxxxxxxxxxxxxxx"
Security Warning

Do not upload your real API key to GitHub.

For a production application, use environment variables instead of directly storing the key in your source code.

Run the Application

Run the following command:

python app.py

After starting the Flask server, open the address displayed in the terminal.

Example
Input
```text
Recipient:
Professor Smith

Purpose:
I need to request leave for three days due to a family function.

Important Points:
Leave from 5th October to 7th October.
I will complete pending assignments.

Tone:
Professional

Length:
Medium
```
Generated Subject
Request for Leave from 5th to 7th October
Generated Email
```text
Dear Professor Smith,

I am writing to request leave from 5th October to 7th October as I need to attend an important family function.

I will ensure that my pending assignments are completed and that I catch up with any academic work missed during this period.

I kindly request you to grant me leave for these three days.

Thank you for your consideration.

Regards,
Your Name
```
Use Cases

MailCraft AI can be useful for:

Students
Employees
Job applicants
Professionals
Businesses
Leave requests
Job applications
Internship communication
Meeting requests
Follow-up emails
Formal requests
Academic communication
Future Improvements

Potential future enhancements include:

Multiple subject suggestions
Email rewriting
Grammar correction
Email summarization
Common email templates
Gmail integration
Outlook integration
User accounts
Saved emails
PDF export
Multiple language support
Disclaimer

AI-generated content should be reviewed before sending. Users should verify names, dates, facts, and other important information.

Author

Subhajit Pramanick

Built using Flask, Python, Groq API, Requests, HTML, CSS, and JavaScript.

<img width="1880" height="970" alt="Screenshot 2026-09-30 210142" src="https://github.com/user-attachments/assets/60912dea-d0cf-4884-a1b3-504a9b425ea7" />

<img width="1887" height="962" alt="Screenshot 2026-09-30 210208" src="https://github.com/user-attachments/assets/66c55b01-e4e1-4927-b33f-67889e28c4a8" />

