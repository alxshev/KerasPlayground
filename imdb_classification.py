from tensorflow import keras

(train_data, train_labels), (test_data, test_labels) = keras.datasets.imdb.load_data(num_words=10000)
print("hello")