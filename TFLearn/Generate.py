import tensorflow as tf
from Model import *


with tf.Session(graph=tf.Graph()) as sess:
    tf.saved_model.loader.load(sess, [tf.saved_model.tag_constants.SERVING], './models')
    
    # get a handle to the module
    m = tf.get_default_graph().get_tensor_by_name('m:0')


text = m.generate(15, "a", 0.5)
print("Text: ", text)
    
del m