from tflite_runtime.interpreter import Interpreter
import numpy as np
# import argparse
from PIL import Image
import os 

# new variable and directory definitions
image_directory = "image"
filename = "image.jpg"
image_path = os.path.join(image_directory, filename)
model_directory = "mobilenet_v1_1.0_224_quant_and_labels"
model_file = "mobilenet_v1_1.0_224_quant.tflite"
model_path = os.path.join(model_directory, model_file)
label_file= "labels_mobilenet_quant_v1_224.txt"
label_path = os.path.join(model_directory, label_file)
top_k_results = 3


if not os.path.exists(label_path):
    print(label_path)
    raise FileNotFoundError(f"Label file not found at: {label_path}")
if not os.path.exists(model_path):
    print(model_path)
    raise FileNotFoundError(f"Label file now found at: {model_path}")

with open(label_path, 'r') as f:
    labels = list(map(str.strip, f.readlines()))

# Load TFLite model and allocate tensors
interpreter = Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Read image
img = Image.open(image_path).convert('RGB')

# Get input size
input_shape = input_details[0]['shape']
size = input_shape[:2] if len(input_shape) == 3 else input_shape[1:3]

# Preprocess image
img = img.resize(size)
img = np.array(img)

# Add a batch dimension
input_data = np.expand_dims(img, axis=0)

# Point the data to be used for testing and run the interpreter
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

# Obtain results and map them to the classes
predictions = interpreter.get_tensor(output_details[0]['index'])[0]

# Get indices of the top k results
top_k_indices = np.argsort(predictions)[::-1][:top_k_results]

def show_results():
    results = ""
    for i in range(top_k_results):
        results += f"{labels[top_k_indices[i]], predictions[top_k_indices[i]] / 255.0}\n"
    return results


