import os
from flask import *
from werkzeug.utils import secure_filename

# Retrieve absolute path of directory 
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# Specify location to save images temporary
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# default getway when script run
@app.route('/')
def upload_image():
    return render_template('index.html')

# perofm image upload and display 
@app.route('/img/',methods=['POST'])
def submit_image():
    #retrieve file from post request data
    image = request.files['picture']
    filename = secure_filename(image.filename)
    # save image temporary
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #send image back to user as a response
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
