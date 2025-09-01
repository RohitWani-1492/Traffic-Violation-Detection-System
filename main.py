from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response
from flask_mail import Mail, Message
import os
from werkzeug.utils import secure_filename
import cv2
import subprocess
from sqldb1 import get_stored_license_plates
from PIL import Image, ImageDraw, ImageFont
import random
from integrated import detect_violations

app = Flask(__name__)

# ✅ Mail Configuration
app.config['SECRET_KEY'] = "tsfyguaistyatuis589566875623568956"
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "itstisha.naw24@gmail.com"
app.config['MAIL_PASSWORD'] = "nrzffwuacixmowzd"

mail = Mail(app)

UPLOAD_FOLDER = 'static/uploads'
CHALLAN_FOLDER = "static/challans"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CHALLAN_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CHALLAN_FOLDER'] = CHALLAN_FOLDER

FFMPEG_PATH = "C:\\ffmpeg\\bin\\ffmpeg.exe"  # Explicit FFmpeg path


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp4', 'avi', 'mov'}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '' or not allowed_file(file.filename):
            return redirect(request.url)

        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        return redirect(url_for('process_video', filename=filename))

    return render_template('index.html')


@app.route('/process_video/<filename>')
def process_video(filename):
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    output_filename = f"output_{filename}"
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

    cap = cv2.VideoCapture(input_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        detect_violations(frame)
        out.write(frame)  # Make sure to write frames to the output video

    cap.release()
    out.release()

    # ✅ Convert MP4 to WEBM after processing is complete
    webm_filename = f"output_{filename.split('.')[0]}.webm"
    webm_path = os.path.join(app.config['UPLOAD_FOLDER'], webm_filename)

    ffmpeg_command = [
        FFMPEG_PATH, "-i", output_path,
        "-c:v", "libvpx-vp9", "-b:v", "1M", "-c:a", "libopus",
        webm_path
    ]
    subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # ✅ Send bulk emails after conversion
    send_bulk_emails()

    return render_template(
        'index.html',
        input_video=filename,
        output_video=webm_filename  # Serve the WEBM video
    )



@app.route("/challan/<plate>")
def view_challan(plate):
    """Allows users to view/download their challan as a PNG."""
    challan_path = os.path.join(app.config["CHALLAN_FOLDER"], f"challan_{plate}.png")

    if not os.path.exists(challan_path):
        return "Challan not found", 404

    return send_from_directory(app.config["CHALLAN_FOLDER"], f"challan_{plate}.png")


def send_bulk_emails():
    """Fetch stored license plates and send emails with PNG challan attachment."""
    stored_plates = get_stored_license_plates()  # Fetch stored plates from MongoDB

    if not stored_plates:
        print("⚠️ No stored plates found. Skipping email notifications.")
        return

    for plate, violation_type in stored_plates:
        email = f"{plate}@gmail.com"  # Dummy email format (modify as needed)
        challan_path = os.path.join(app.config['CHALLAN_FOLDER'], f"challan_{plate}.png")

        if not os.path.exists(challan_path):
            generate_challan_image(plate, violation_type, challan_path)

        send_email(email, plate, challan_path)


def send_email(email, plate_number, challan_path):
    """Sends an email with the challan PNG attachment."""
    msg_title = "Traffic Violation - Challan Notification"
    sender = "noreply@app.com"
    msg_body = f"A challan has been generated for vehicle {plate_number}. Please clear your dues."

    msg = Message(msg_title, sender=sender, recipients=[email])
    msg.html = render_template("email.html", data={'title': msg_title, 'body': msg_body})

    with open(challan_path, "rb") as f:
        msg.attach(f"challan_{plate_number}.png", "image/png", f.read())

    try:
        mail.send(msg)
        print(f"Email sent to {email} for plate {plate_number} with challan attached.")
    except Exception as e:
        print(f"Failed to send email to {email}: {e}")


def generate_challan_image(plate_number, violation_type, save_path):
    """Generates a PNG challan with violation details."""
    challan_number = f"MKA{random.randint(10000, 99999)}"
    img_width, img_height = 700, 400
    img = Image.new('RGB', (img_width, img_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 28)
        header_font = ImageFont.truetype("arial.ttf", 20)
        text_font = ImageFont.truetype("arial.ttf", 18)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        text_font = ImageFont.load_default()

    # Title
    title_text = "TRAFFIC VIOLATION"
    title_width = draw.textlength(title_text, font=title_font)
    draw.text(((img_width - title_width) // 2, 10), title_text, fill="blue", font=title_font)

    # Table: Section, Offence, Fine
    # Table Data
    table_x = 50
    y_start = 50

    headers = ["Section", "Offence", "Fine"]
    values = ["129/177 MVA", violation_type, "200"]

    details_headers = ["Challan No", "Vehicle No"]
    details_values = [challan_number, plate_number]

    # Draw Table
    cell_widths = [150, 250, 100]
    cell_height = 40

    # Draw Header Row
    x = table_x
    y = y_start
    for i, header in enumerate(headers):
        draw.rectangle([x, y, x + cell_widths[i], y + cell_height], outline="black")
        draw.text((x + 10, y + 10), header, fill="black", font=text_font)
        x += cell_widths[i]

    # Draw Value Row
    x = table_x
    y += cell_height
    for i, value in enumerate(values):
        draw.rectangle([x, y, x + cell_widths[i], y + cell_height], outline="black")
        draw.text((x + 10, y + 10), value, fill="black", font=text_font)
        x += cell_widths[i]

    # Draw Details Table
    y += cell_height + 20  # Spacing after first table
    for i, (header, value) in enumerate(zip(details_headers, details_values)):
        draw.rectangle([table_x, y, table_x + 200, y + cell_height], outline="black")
        draw.text((table_x + 10, y + 10), header, fill="black", font=text_font)

        draw.rectangle([table_x + 200, y, table_x + 500, y + cell_height], outline="black")
        draw.text((table_x + 210, y + 10), value, fill="black", font=text_font)

        y += cell_height

    # Save as PNG
    img.save(save_path)
    print(f"✅ Challan PNG saved at: {save_path}")


# Serve uploaded video files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
