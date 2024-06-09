App Link :- https://holographic-microplastic-image-classification-cnn.streamlit.app/

# Microplastic Classification using Holographic Images

This Streamlit application classifies a given holographic image of microplastics into one of the following categories using a Convolutional Neural Network (CNN) model built with PyTorch:

- Low-Density Polyethylene (LDPE) with dust
- Polyethylene (PE)
- Polyethylene (PE) with dust
- Polyhydroxyalkanoate (PHA)
- Polyhydroxyalkanoate (PHA) with dust
- Polystyrene (PS)
- Polystyrene (PS) with dust
- Mixed Plastic (combination of different types)
- None (if it doesn't belong to any of these plastic types)

After classification, the application uses the Gemni API to generate content regarding the classified microplastic, including its impact on the world's oceans and possible treatment methods.

## Tech Stack

- **Python**: Streamlit, PyTorch
- **Deep Learning Model**: CNN
- **Frontend**: HTML, CSS

## Features

1. **Microplastic Classification**: Classifies the holographic image into one of the predefined categories.
2. **Content Generation**: Generates information about the identified microplastic type, its environmental impact, and treatment methods using the Gemni API.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/microplastic-classification.git
    cd microplastic-classification
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Upload a holographic image of a microplastic.

3. View the classification results and generated content.

## Model

The Convolutional Neural Network (CNN) model is trained using PyTorch to classify the microplastics. The model achieves high accuracy in distinguishing between different types of microplastics and their variants with dust.

## API Integration

The Gemni API is used to generate detailed content about the classified microplastic, including:

- What is the classified microplastic?
- How it affects the world's oceans.
- How it can be treated.


## Dataset

This dataset contains microplastic particle images used for research purposes, including 'Holographic Classifier: Deep Learning in Digital Holography for Automatic Micro-objects Classification' and 'Microplastic pollution monitoring with holographic classification and deep learning.' The dataset is labeled by microplastic type and number of particles in the image.

[Dataset Source](https://github.com/ymzhu19eee/dataset_microplastics)
