import tensorflow as tf
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg19 import preprocess_input
from keras.applications.vgg19 import decode_predictions
import glob

model = tf.keras.models.load_model('./pretrained_model/model.h5', compile=False)

def preprocess(image):
    r'''
    Preprocess an image to make it ready-to-use by VGG19
    '''
    
    image = img_to_array(image)     # convert the image pixels to a numpy array    
    image = image.reshape(
                        (1, image.shape[0], image.shape[1], image.shape[2])
                        )           # reshape data for the model
    image = preprocess_input(image) # prepare the image for the VGG model

    return image

def predict(image):
    r'''
    Predict the class of a given image 
    '''
    
    yhat = model.predict(image)         # predict the probability across all output classes    
    label = decode_predictions(yhat)    # convert the probabilities to class labels    
    label = label[0][0]                 # retrieve the most likely result, e.g. highest probability    
    prediction = label[1]               # return the classification
    percentage = '%.2f%%' % (label[2]*100)

    return prediction, percentage

def test(image_f):
    r'''
    Test the functionality
    '''
    image = load_img(image_f, target_size=(224, 224))
    image = preprocess(image)
    prediction, percentage = predict(image)
    print(f"\n {image_f} -> {prediction} : {percentage}")

if __name__ == '__main__':
    ''' for test'''
    files = glob.glob('./test-images/*.jpg')
    for f in files:
        test(f)
    