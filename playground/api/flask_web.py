"""
A basic web API to fetch email data using the Flask framework. 

Endpoints:
    /get-mail/<mailbox_id>
        Method: GET
        Query Parameters:
            is_read: bool

Create and run Flask app with python -m <path>.<to>.<module>.
Test GET endpoint with 127.0.0.1:5000/<endpoint>.
"""

from typing import Dict, Tuple

from flask import abort, Flask, jsonify, request


# Create the app
app = Flask(__name__)


@app.route("/get-mail/<mailbox_id>", methods=["GET"])
def get_mail(mailbox_id: int) -> Tuple[Dict, int]:
    """
    GET /get-mail/<mailbox_id>
    Retrieves mail from a mailbox. 

    Query Parameters:
        is_read (str): Only fetch mail that has been read.

    Returns:
        Mail as a JSON-formatted response.

    Example:
        python -m <path>.<to>.<module>
        http://127.0.0.1:5000/get-mail/1?is_read=0
    """
    # Simulate data object that would be fetched from database
    mail = {
        "mailbox_id": mailbox_id,
        "emails": [
            {
                "id": "1",
                "from": "sender1@example.com",
                "to": "user1@example.com",
                "subject": "This is a sample subject",
                "body": "This is a sample email body",
                "date": "2023-08-15 12:34:56",
                "is_read": False,
            },
        ],
    }
    # Check for and handle additional parameters
    is_read = request.args.get("is_read")
    if is_read is not None:
        if is_read.lower() in ["1"]:
            is_read = True
        elif is_read.lower() in ["0"]:
            is_read = False
        else:
            abort(400, description=(
                "Invalid value for is_read parameter; expected '1', or '0'"
            ))
        mail = [email for email in mail["emails"] 
                if email["is_read"] == is_read]
    # Return mailbox contents as JSON
    return jsonify(mail), 200


if __name__ == "__main__":
    app.run(debug=True)
