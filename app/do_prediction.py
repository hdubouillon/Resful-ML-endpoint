# Imports
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import tensorflow.keras as keras


def predict(flatten_image):
    """
    Return the classification result of a row of pixels. 

    Args:
        flatten_image (tuple, list, np.array): The row of pixels
    """
    
    # load the model
    model = load_model('app/model/best_dense_nn_fashion_mnist')
    # do the prediction
    flatten_image = pd.DataFrame([flatten_image])
    prediction = model.predict(flatten_image/255)
    prediction = np.argmax(prediction, axis=1)
    prediction = prediction[0]
    
    return prediction


if __name__ == "__main__":
    pass