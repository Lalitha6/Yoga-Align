# Yoga Website

## Overview
This is a professional yoga-themed web application built using Flask. The application provides users with information about yoga classes, schedules, and the studio itself. It features a modern design with glassmorphism aesthetics and is fully responsive.

## Features
- Home page with high-quality yoga images and login/signup forms.
- About page detailing the yoga studio's mission and values.
- Classes page listing available yoga classes.
- Contact page with a form for inquiries.
- Schedule page displaying class timings.

## Technologies Used
- Flask: A lightweight WSGI web application framework.
- Flask-WTF: An extension for Flask that simplifies form handling.
- HTML/CSS/JavaScript: For front-end development.
- SQLite: For database management (or any other database as configured).

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd yoga-website
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Set up the database (if applicable):
   ```
   python -m app.models
   ```
5. Run the application:
   ```
   flask run
   ```

## Usage
- Access the application in your web browser at `http://127.0.0.1:5000/`.
- Use the navigation links to explore different sections of the website.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.