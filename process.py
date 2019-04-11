import numpy as np

from keras.models import Sequential
from data_preprocessing import my_DataGenerator

# Parameters
params = {'dim': (32,32,32),
          'batch_size': 64,
          'n_classes': 2,
          'n_channels': 1,
          'shuffle': True}

# Datasets
data = np.load('data.npy')
data_list = data['item']
labels = data['label']# Labels
# random
index = np.random.permutation(len(labels))
random_data = data[index]
random_labels = labels[index]
# train and validation
train_size = 25000
partition = {}
partition['train'] = [x for x in range(train_size)]# IDs of train
partition['validation'] = [x for x in range(train_size,len(index))]# IDs of validation

# Generators
training_generator = my_DataGenerator(partition['train'], random_data, random_labels, **params)
validation_generator = my_DataGenerator(partition['validation'], random_data, labels, **params)

# Design model
model = Sequential()
[...] # Architecture
model.compile()

# Train model on dataset
model.fit_generator(generator=training_generator,
                    validation_data=validation_generator,
                    use_multiprocessing=True,
                    n_workers=6)
