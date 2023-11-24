import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as display
import PIL.Image as Image
import urllib.request
import os
import zipfile
import time

def deep_dream_single_function(url, max_dim=500, steps=100, step_size=0.01):
    def download(url, max_dim=None):
        name = url.split('/')[-1]
        image_path = tf.keras.utils.get_file(name, origin=url)
        img = Image.open(image_path)
        if max_dim:
            img.thumbnail((max_dim, max_dim))
        return np.array(img)

    def deprocess(img):
        img = 255 * (img + 1.0) / 2.0
        return tf.cast(img, tf.uint8)

    def show(img):
        display.display(Image.fromarray(np.array(img)))

    def deep_dream(img, steps=100, step_size=0.01):
        img = tf.keras.applications.inception_v3.preprocess_input(img)
        img = tf.convert_to_tensor(img)
        step_size = tf.convert_to_tensor(step_size)
        steps_remaining = steps
        step = 0
        while steps_remaining:
            if steps_remaining > 100:
                run_steps = tf.constant(100)
            else:
                run_steps = tf.constant(steps_remaining)
            steps_remaining -= run_steps
            step += run_steps

            loss, img = deepdream(img, run_steps, tf.constant(step_size))

            display.clear_output(wait=True)
            show(deprocess(img))
            print("Step {}, loss {}".format(step, loss))

        result = deprocess(img)
        display.clear_output(wait=True)
        show(result)

        return result

    def run_deep_dream_simple(img, steps=100, step_size=0.01):
        img = deep_dream(img, steps, step_size)
        return img

    url = 'https://storage.googleapis.com/download.tensorflow.org/example_images/YellowLabradorLooking_new.jpg'
    original_img = download(url, max_dim=max_dim)
    show(original_img)

    base_model = tf.keras.applications.InceptionV3(include_top=False, weights='imagenet')
    names = ['mixed3', 'mixed5']
    layers = [base_model.get_layer(name).output for name in names]

    dream_model = tf.keras.Model(inputs=base_model.input, outputs=layers)

    deepdream = deep_dream(dream_model)

    img = run_deep_dream_simple(img=original_img, steps=steps, step_size=step_size)

    start = time.time()
    OCTAVE_SCALE = 1.30

    img = tf.constant(np.array(original_img))
    base_shape = tf.shape(img)[:-1]
    float_base_shape = tf.cast(base_shape, tf.float32)

    for n in range(-2, 3):
        new_shape = tf.cast(float_base_shape * (OCTAVE_SCALE ** n), tf.int32)

        img = tf.image.resize(img, new_shape).numpy()

        img = run_deep_dream_simple(img=img, steps=50, step_size=0.01)

    display.clear_output(wait=True)
    img = tf.image.resize(img, base_shape)
    img = tf.image.convert_image_dtype(img / 255.0, dtype=tf.uint8)
    show(img)

    end = time.time()
    print("Time taken:", end - start)

deep_dream_single_function('https://storage.googleapis.com/download.tensorflow.org/example_images/YellowLabradorLooking_new.jpg', max_dim=500, steps=100, step_size=0.01)
