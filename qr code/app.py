from flask import Flask, render_template, request, send_file
import qrcode
from fpdf import FPDF
import os
import firebase_admin
from firebase_admin import credentials, storage

app = Flask(__name__, template_folder='template')

# Initialize Firebase Admin SDK (use your own credentials)
cred = credentials.Certificate('C:/Users/user/Desktop/qr code/firebase_key.json')

firebase_admin.initialize_app(cred, {
    'storageBucket': 'pdftaking.appspot.com'
})

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/generate-text', methods=['POST'])
def generate_text_qr():
    qr_img_filename = 'temp_qrcode_text.png'  # Initialize filename here
    try:
        text = request.form['text']

        if not text:
            return "Please provide text to generate a QR code."

        # Generate QR Code for the Text
        qr = qrcode.make(text)
        qr.save(qr_img_filename)

        # Create PDF and insert the QR code image
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Your QR Code for Text", ln=True, align="C")
        pdf.image(qr_img_filename, x=60, y=30, w=90)

        # Save the PDF directly to a file
        pdf_filename = 'text_qr.pdf'
        pdf.output(pdf_filename)

        return send_file(pdf_filename, as_attachment=True)

    except Exception as e:
        print(f"Error generating QR code for text: {e}")
        return "Error generating QR code for text."
    
    finally:
        if os.path.exists(qr_img_filename):
            os.remove(qr_img_filename)
@app.route('/main')
def main_page():
    return render_template('main.html')
@app.route('/generate-contact', methods=['POST'])
def generate_contact_qr():
    qr_img_filename = 'temp_qrcode_contact.png'  # Define this at the beginning
    try:
        # Correct field names to match your HTML form
        name = request.form['name']
        contact1 = request.form['contact1']  # Make sure this matches the HTML input name
        contact2 = request.form.get('contact2')  # Use the correct name
        call_time = request.form.get('call_time')  # Use the correct name

        # Debugging output to check received data
        print(f"Received: Name={name}, Contact1={contact1}, Contact2={contact2}, Call Time={call_time}")

        # Validate inputs
        if not name or not contact1:
            return "Please provide contact information."

        contact_info = f"Name: {name}\nContact 1: {contact1}"
        if contact2:
            contact_info += f"\nContact 2: {contact2}"
        if call_time:
            contact_info += f"\nBest Call Time: {call_time}"

        # Generate QR Code for Contact Info
        qr = qrcode.make(contact_info)

        # Save QR code as an image to disk temporarily
        qr.save(qr_img_filename)

        # Create PDF and insert the QR code image
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Your QR Code for Contact Info", ln=True, align="C")
        pdf.image(qr_img_filename, x=60, y=30, w=90)

        # Save the PDF directly to a file
        pdf_filename = 'contact_qr.pdf'
        pdf.output(pdf_filename)

        return send_file(pdf_filename, as_attachment=True)

    except Exception as e:
        print(f"Error generating QR code for contact: {e}")
        return f"Error generating QR code for contact: {e}"

    finally:
        # Clean up the temporary QR code image file if it exists
        if os.path.exists(qr_img_filename):
            os.remove(qr_img_filename)

@app.route('/generate-link', methods=['POST'])
def generate_link_qr():
    qr_img_filename = 'temp_qrcode.png'  # Initialize filename here
    try:
        link = request.form['link']

        if not link or not link.startswith("http"):
            return "Please provide a valid link."

        # Generate QR Code for the Link
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(qr_img_filename)

        # Create PDF and insert the QR code image
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Your QR Code for the Link", ln=True, align="C")
        pdf.image(qr_img_filename, x=60, y=30, w=90)

        # Save the PDF directly to a file
        pdf_filename = 'qrcode.pdf'
        pdf.output(pdf_filename)

        return send_file(pdf_filename, as_attachment=True)

    except Exception as e:
        print(f"Error generating QR code for link: {e}")
        return "Error generating QR code for link."
    
    finally:
        if os.path.exists(qr_img_filename):
            os.remove(qr_img_filename)

@app.route('/generate-pdf', methods=['POST'])
def upload_pdf():
    qr_img_filename = 'temp_qrcode.png'  # Define this at the beginning
    try:
        # Get the uploaded PDF file
        pdf_file = request.files['pdf_file']

        # Validate the uploaded file
        if not pdf_file or not pdf_file.filename.endswith('.pdf'):
            return "Please upload a valid PDF file."

        # Firebase Storage bucket
        bucket = storage.bucket()

        # Upload the PDF file to Firebase Storage
        blob = bucket.blob(f"pdfs/{pdf_file.filename}")
        blob.upload_from_file(pdf_file)
        blob.make_public()
        pdf_url = blob.public_url

        # Generate QR code for the PDF link
        qr = qrcode.make(pdf_url)

        # Save QR code as an image to disk temporarily
        qr.save(qr_img_filename)

        # Create PDF and insert the QR code image
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Your QR Code for PDF file", ln=True, align="C")
        pdf.image(qr_img_filename, x=60, y=30, w=90)

        # Save the PDF directly to a file
        pdf_filename = 'pdf_qr.pdf'
        pdf.output(pdf_filename)

        return send_file(pdf_filename, as_attachment=True)

    except Exception as e:
        print(f"Error uploading PDF and generating QR code: {e}")
        return f"Error generating QR code for the PDF: {e}"

    finally:
        # Clean up the temporary QR code image file if it exists
        if os.path.exists(qr_img_filename):
            os.remove(qr_img_filename)


if __name__ == '__main__':
    app.run(debug=True)
