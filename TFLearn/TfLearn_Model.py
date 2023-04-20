import tflearn
from tflearn.data_utils import *
from parentdirectory import Constants

class Model:
    def __init__(self, path, maxlen=25, checkpoint_path='model.ckpt', model_path='model.tfl'):
        self.path = path
        self.maxlen = maxlen
        self.checkpoint_path = checkpoint_path
        self.model_path = model_path
        self.char_idx = None
        self.model = None
    
    def preprocess_data(self):
        # Load and preprocess the text data
        X, Y, char_idx = textfile_to_semi_redundant_sequences(self.path, seq_maxlen=self.maxlen, redun_step=1)
        self.char_idx = char_idx
        return X, Y
    
    def build_model(self):
        # Define the network architecture
        input_layer = tflearn.input_data(shape=[None, self.maxlen, len(self.char_idx)])
        lstm_layer = tflearn.lstm(input_layer, 256)
        output_layer = tflearn.fully_connected(lstm_layer, len(self.char_idx), activation='softmax')
        net = tflearn.regression(output_layer, optimizer='adam', loss='categorical_crossentropy')
        self.model = tflearn.SequenceGenerator(net, dictionary=self.char_idx,
                                               seq_maxlen=self.maxlen,
                                               clip_gradients=5.0,
                                               checkpoint_path=self.checkpoint_path)
    
    def train_model(self, X, Y, val_split=0.1, batch_size=128, epochs=30, run_id='text_generation'):
        # Train the model
        self.model.fit(X, Y, validation_set=val_split, batch_size=batch_size, n_epoch=epochs, run_id=run_id)
        
        # Save the model checkpoint to disk
        self.model.save(self.checkpoint_path)
        
        # Save the final trained model to disk
        self.model.save(self.model_path)
    
    def generate_text(self, seed, length=100, temperature=0.5):
        # Generate text
        return self.model.generate(length, 
                                   temperature=temperature, 
                                   seq_seed=seed)
