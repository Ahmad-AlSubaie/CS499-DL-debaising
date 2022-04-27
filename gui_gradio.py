import gradio as gr
import numpy as np
import tensorflow as tf
import tensorflow_text as text


dataset_name = 'BERT/hate_speech'
saved_model_path = './{}_bert'.format(dataset_name.replace('/', '_'))

# reloaded_model = tf.saved_model.load("BERT/hate_speech_bert")


def predict(text):
    return np.argmax(classifier_model.predict(text), axis=-1)


demo = gr.Interface(fn=predict, inputs="text", outputs="text")

if __name__ == "__main__":
    demo.launch()