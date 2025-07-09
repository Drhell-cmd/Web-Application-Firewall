# Web Application Firewall (WAF) Mini Project

## Project Overview
This project is a simple web application built with Flask that demonstrates the use of a custom Web Application Firewall (WAF) filter. The WAF is designed to block potentially malicious user input and log blocked attempts.

## How It Works
- The application provides a web form for user input on the main page (`/`).
- When a user submits input, the `waf_filter` function (defined in `waf.py`) checks the input for suspicious or dangerous content.
- If the input is considered unsafe, the WAF blocks the request, displays a blocked message (🚫Blocked by WAF!), and logs the attempt in `blocked.log`.
- If the input is safe, it is accepted and displayed back to the user.

## Files
- `app.py`: Main Flask application.
- `waf.py`: Contains the WAF filter logic.
- `blocked.log`: Stores logs of blocked input attempts.
- `templates/index.html`: HTML template for the web form.

## Usage
1. **Install dependencies:**
   - Make sure you have Python and Flask installed. You can install Flask with:
     ```powershell
     pip install flask
     ```
2. **Run the application:**
   - In your terminal, run:
     ```powershell
     python app.py
     ```
3. **Access the app:**
   - Open your browser and go to `http://127.0.0.1:5000/`.
   - Enter input in the form and submit.
   - If the input is blocked, you will see a blocked message. Otherwise, your input will be displayed.

## Purpose
This project is intended for educational purposes to demonstrate basic WAF concepts and input validation in web applications. It is not intended for production use.
