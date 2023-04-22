import tensorflow as tf
from Model import *

#init and train
m = Model("DataSet.text")
m.train(10)

#save the class
builder = tf.saved_model.builder.SavedModelBuilder('./models')
builder.add_meta_graph_and_variables(tf.get_default_session(), [tf.saved_model.tag_constants.SERVING], {'m': m})
builder.save()

print("--- Model Traind & Saved ---")
del m