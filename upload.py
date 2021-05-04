from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from keras.preprocessing.image import load_img
from model import preprocess, predict

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

# Path for saving uploaded images
app.config['UPLOADED_PHOTOS_DEST'] = './static/img'
configure_uploads(app, photos)

@app.route('/home', methods=['GET', 'POST'])
def home():
    welcome = '''<div style="display: flex; justify-content: center; align-items: center;margin:20%;">
        <h1> Hello! </h1>
        </div>'''
    return welcome

# Main route for upload and prediction
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        
        filename = photos.save(request.files['photo'])  # Save image
        
        image = load_img('./static/img/'+filename, target_size=(224, 224)) # Load image
        
        image = preprocess(image)    # Process image
        
        prediction, percentage = predict(image)    # Make a prediction
        # Render the prediction to the user
        answer = '''
        <div style="display: flex; justify-content: center; align-items: center;margin:20%;">
        
        <h1 style="color:red;"> {} : {}</h1>
        </div>'''.format(prediction, percentage)

        return answer
    
    return render_template('upload.html')  # Default upload web page to show before the POST request

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)