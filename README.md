Here’s a revised version of your README file, incorporating the removal of the PDF generation feature while maintaining clarity and coherence:

---

# QR Code Generator

## Overview

The QR Code Generator is a web application designed to simplify the process of generating QR codes for various purposes. Whether it’s for personal, professional, or business use, this application allows users to create QR codes from URLs and contact information. The application is built using Flask for the back-end and features a clean, user-friendly front-end interface using HTML, CSS, and JavaScript.

## Features

- **Generate QR Codes**: Create QR codes from URLs and contact information.
- **Contact Information QR Codes**: Input name, contact numbers, and call preferences to generate a QR code for contact details.
- **Responsive Design**: Fully responsive user interface for use on desktops, tablets, and smartphones.
- **Clear Input Instructions**: User guidance is provided on how to input the correct data format.

## Purpose

The purpose of this project is to provide an easy-to-use and efficient tool for generating QR codes in various formats, enhancing the ability to share information digitally. Whether for personal, marketing, or business uses, this solution helps users create and distribute QR codes quickly and effectively.

## Technology Stack

The project utilizes the following technologies:

### Front-End:

- **HTML5, CSS3**: For structuring and styling the user interface.
- **JavaScript**: To handle interactivity and dynamic content updates.

### Back-End:

- **Flask**: A lightweight Python web framework used to handle requests and generate QR codes.

### Python Libraries:

- **qrcode**: For generating QR codes from user input.

### Database:

- **Firebase (if applicable)**: For user authentication and data storage.

## Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- pip package manager installed.
- Create a Firebase project if user authentication is needed.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/qr-code-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd qr-code-generator
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```

## Usage

### Generate QR Codes:

1. Open the app in your browser.
2. Select the input type (URL or contact information).
3. Enter the necessary data.
4. Click the "Generate" button to create the QR code.

### Download QR Codes:

- After generating the QR code, you can share or utilize the QR code as needed.

## Project Structure

```
├── app.py                  # Main Flask application
├── templates/              # HTML templates for front-end
├── static/                 # Static files (CSS, JS, images)
├── firebase_key.json       # Firebase key (optional)
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── qr_code/                # QR code generation logic
```

---

Feel free to adjust any section further or let me know if you’d like to include more details!
