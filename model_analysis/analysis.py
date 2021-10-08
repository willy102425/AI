import tensorflow.keras as keras
import numpy as np

model_path = "../Keras/VGG-16/model_archive/VGG-16_Cifar10.h5"
model = keras.models.load_model(model_path)
model.summary()

for layer in model.layers:
    if ( len(layer.get_weights())>1 ) :
        weights = layer.get_weights()[0]
        biases  = layer.get_weights()[1]
        print( len(weights) )
        # print( weights )
        # config = layer.get_config()
        # print( config )

print( model.layers[0].get_config() )