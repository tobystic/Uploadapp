from flask import Flask, request, render_template

app = Flask(__name__, template_folder='./')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part in the request"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    # You can customize the file storage location and handling here
    # For this example, let's just save the file in the same directory
    file.save(file.filename)
    return "File uploaded successfully!"

if __name__ == '__main__':
    app.run(debug=True)
