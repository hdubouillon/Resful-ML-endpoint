# Imports
from tensorflow.keras.models import load_model, save_model
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import tensorflow.keras as keras

import pandas as pd
import numpy as np


# The path for the new data
new_training_data_path = 'app/data/fashion-mnist-train-2.csv'


def update_model_pipeline(new_training_data_path):
    """
    Re-train the model with new data.
    If the new model is better, use it to replace the old one.

    Args:
        new_training_data_path (str): The path for the new data
    """
    
    # Load data
    train = pd.read_csv(new_training_data_path)
    test = pd.read_csv('app/data/fashion-mnist_test.csv')

    # Create X and y for train and test
    X_train = train.drop(columns='label')
    X_test = test.drop(columns='label')
    y_train = train['label']
    y_test = test['label']

    # Scale data
    X_train = X_train / 255.0
    X_test = X_test / 255.0

    # Load the best model
    model = load_model('app/model/best_dense_nn_fashion_mnist')
    best_model = model

    # Train the model with the new data
    es = EarlyStopping(monitor='accuracy', mode='auto', verbose=0, patience=20)
    mc = ModelCheckpoint('app/model/new_dense_nn_fashion_mnist', monitor='val_accuracy', mode='max', verbose=0, save_best_only=True)
    model.compile(optimizer='adam', loss ='sparse_categorical_crossentropy', metrics = ['accuracy'])
    history = model.fit(X_train, y_train, validation_split=0.2, epochs=500, batch_size=256, callbacks=[es, mc])

    # Calculate the new accuracy for both models
    _, model_accuracy = model.evaluate(X_test, y_test, verbose=0)
    _, best_model_accuracy = best_model.evaluate(X_test, y_test, verbose=0)

    # Import the new model and the predictions if the new model outperfom the old one
    if model_accuracy > best_model_accuracy:
        print(f'Accuracy improved from: {best_model_accuracy} to: {model_accuracy}')
        y_pred = model.predict(X_test)
        pd.Series(np.argmax(y_pred, axis=1)).to_csv('app/predictions/best_predictions_fashion_mnist.csv', index=False)
        save_model(model, 'app/model/best_dense_nn_fashion_mnist')


if __name__ == "__main__":
    update_model_pipeline(new_training_data_path)