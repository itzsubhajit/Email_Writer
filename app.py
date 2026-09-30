from flask import Flask, request, render_template
import requests

app = Flask(__name__)

api_key = "ADD YOUR OWN API KEY"


@app.route("/", methods=["GET", "POST"])
def home():

    subject = ""
    email_body = ""
    error = ""

    if request.method == "POST":

        recipient = request.form.get("recipient", "").strip()
        purpose = request.form.get("purpose", "").strip()
        key_points = request.form.get("key_points", "").strip()
        tone = request.form.get("tone", "Professional")
        length = request.form.get("length", "Medium")

        # Check required fields
        if not recipient or not purpose:
            error = "Please enter the recipient and email purpose."

        else:

            prompt = f"""
You are a professional email writing assistant.

Write a polished professional email based on the information below.

Recipient:
{recipient}

Purpose of the email:
{purpose}

Important points to include:
{key_points if key_points else "No additional points provided."}

Tone:
{tone}

Length:
{length}

Your task is to generate:
1. One professional and relevant email subject.
2. A complete email body.

Follow these formatting rules strictly:

SUBJECT: <write only one subject line>

BODY:
<write the complete email>

The email body should:
- Have a professional greeting.
- Clearly explain the purpose.
- Include the important points naturally.
- Be polite and professional.
- Have proper paragraphs.
- End with an appropriate professional closing.
- Do not add explanations outside SUBJECT and BODY.
"""

            try:

                response = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "openai/gpt-oss-20b",
                        "messages": [
                            {
                                "role": "system",
                                "content": "You are an expert professional email writer."
                            },
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ],
                        "temperature": 0.7
                    },
                    timeout=60
                )

                data = response.json()

                if response.ok:

                    generated_text = data["choices"][0]["message"]["content"].strip()



                    if "BODY:" in generated_text:

                        parts = generated_text.split("BODY:", 1)

                        subject_part = parts[0]
                        body_part = parts[1]

                        subject = subject_part.replace(
                            "SUBJECT:", ""
                        ).strip()

                        email_body = body_part.strip()

                    else:
                        subject = "Professional Email"
                        email_body = generated_text

                else:

                    error = data.get(
                        "error", {}
                    ).get(
                        "message",
                        "Something went wrong with the Groq API."
                    )

            except requests.exceptions.RequestException:
                error = "Unable to connect to the Groq API. Please check your internet connection."

            except Exception as e:
                error = "An unexpected error occurred."

    return render_template(
        "index.html",
        subject=subject,
        email_body=email_body,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)