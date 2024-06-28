# Importando bibliotecas necessárias
import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from yolov8 import YOLOv8
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import random

def load_data(data_path):
    # Carregar dados a partir do caminho fornecido
    images = []
    labels = []
    for file in os.listdir(data_path):
        if file.endswith('.jpg'):
            image = cv2.imread(os.path.join(data_path, file))
            label = file.replace('.jpg', '.txt')
            with open(os.path.join(data_path, label), 'r') as f:
                label_data = f.read()
            images.append(image)
            labels.append(label_data)
    return images, labels

def preprocess_data(images, labels):
    # Pré-processamento de dados
    processed_images = []
    processed_labels = []
    for image, label in zip(images, labels):
        image = cv2.resize(image, (640, 640))
        processed_images.append(image)
        processed_labels.append(label)
    return np.array(processed_images), np.array(processed_labels)

def build_model():
    # Construir o modelo YOLOv8
    model = YOLOv8(input_shape=(640, 640, 3), num_classes=80)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model(model, train_data, val_data, epochs=50, batch_size=32):
    # Treinar o modelo
    history = model.fit(train_data[0], train_data[1], validation_data=val_data,
                        epochs=epochs, batch_size=batch_size)
    return model, history

def evaluate_model(model, test_data):
    # Avaliar o modelo
    results = model.evaluate(test_data[0], test_data[1])
    print(f'Test loss: {results[0]} / Test accuracy: {results[1]}')
    return results

def save_model(model, save_path):
    # Salvar o modelo treinado
    model.save(save_path)

def plot_training_history(history):
    # Plotar histórico de treinamento
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Accuracy')
    plt.plot(history.history['val_accuracy'], label = 'Val Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0, 1])
    plt.legend(loc='lower right')

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Loss')
    plt.plot(history.history['val_loss'], label='Val Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.ylim([0, 1])
    plt.legend(loc='upper right')
    plt.show()

def main():
    data_path = 'path/to/data'
    save_path = 'path/to/save/model'
    
    # Carregar e preprocessar os dados
    images, labels = load_data(data_path)
    images, labels = preprocess_data(images, labels)
    
    # Dividir os dados em conjuntos de treino, validação e teste
    train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)
    train_images, val_images, train_labels, val_labels = train_test_split(train_images, train_labels, test_size=0.25, random_state=42)
    
    # Construir e treinar o modelo
    model = build_model()
    model, history = train_model(model, (train_images, train_labels), (val_images, val_labels))
    
    # Avaliar o modelo
    evaluate_model(model, (test_images, test_labels))
    
    # Salvar o modelo treinado
    save_model(model, save_path)
    
    # Plotar o histórico de treinamento
    plot_training_history(history)

if __name__ == "__main__":
    main()
