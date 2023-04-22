import tflearn
from tflearn.data_utils import *

class Model:
    def __init__(self, path: str):
        #Load and preprocess the text data
        self.path = path
        self.maxlen = 15
        self.char_idx = None
        self.X, self.Y, self.char_idx = textfile_to_semi_redundant_sequences(self.path, seq_maxlen=self.maxlen, redun_step=1)

        # Define the network architecture
        input_layer = tflearn.input_data(shape=[None, self.maxlen, len(self.char_idx)])
        lstm_layer = tflearn.lstm(input_layer, 256)
        output_layer = tflearn.fully_connected(lstm_layer, len(self.char_idx), activation='softmax')
        self.net = tflearn.regression(output_layer, optimizer='adam',
                                loss='categorical_crossentropy')
        
        self.model = tflearn.SequenceGenerator(self.net, dictionary=self.char_idx,
                                        seq_maxlen=self.maxlen,
                                        clip_gradients=5.0,
                                        checkpoint_path='model.ckpt')
        
    def train(self, n_epoch: int) :
        # Train the model
        self.model.fit(self.X, self.Y, validation_set=0.1, batch_size=128,
                n_epoch=n_epoch, run_id='text_generation')
        
    def generate(self, length: int, seed: str, temperature=0.5) :
        #generate text
        return self.model.generate(length, temperature = temperature, seq_seed=seed)
    
    def save(self, filename: str):
        # Save the trained model to a file
        self.model.save(filename)