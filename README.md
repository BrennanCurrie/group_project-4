# group_project-4

## Overview of Analysis

By utilizing large machine learning, we are striving to develop an effective model to accurately predict an animal’s/pet’s mood through facial recognition. We will be categorizing the results into four categories: happy, sad, angry, or other. Our minimum accuracy score goal is 75%. Through trial and error, we used multiple models to determine the most successful and deployed this model. Multiple libraries were read in to complete this model including os, numpy, tensorflow, cv2, keras, sklearn, matplotlib, and google colab.

## Results
*	

## Data Preprocessing
*	Multiple picture files located at https://www.kaggle.com/datasets/anshtanwar/pets-facial-expression-dataset were downloaded for this model.
*	The data was reviewed to determine sample size.
*	The images were resized to fit the model

## Compiling, Training, and Evaluating the Model
*	Using a Keras Sequential model with multiple different activation functions to attempt to increase accuracy. The maximum test accuracy received never exceeded 48%
*	Using a DenseNet model, the test accuracy received increased to approximately 56%
*	Using a VGG16, test accuracy was at approximately 56%
*	Because the data set is small, data augmentation was used to increase the training size of the model. Data Augmentation should not be used for test or validation data. This augmentation made slight changes to the original images giving addition data to run through the training model. 
*	The model was run through different numbers of epochs to determine accuracy and loss levels. We also added an early stop function to stop the epochs if which stopped the training when the accuracy stops improving. A learning rate scheduler was added to assist in determining optimal learning rates. 
*	Line graphs are also provided to show the accuracy and loss over time throughout the different models. They provide a visual representation of peaks valleys, and plateaus in the training.

## Summary

This data set was small which caused difficulty in reaching a high level of test accuracy. To help mitigate its original size, data augmentation was used on the training sets to provide a larger data set without changing the test data. 

## Citations

* Dataset: https://www.kaggle.com/datasets/anshtanwar/pets-facial-expression-dataset
* Starter Code DenseNet, ResNet, EfficientNet: https://www.kaggle.com/code/anshtanwar/resnet-densenet-efficientnet-pet-s-expression
* Starter Code VGG16: https://www.analyticsvidhya.com/blog/2020/08/top-4-pre-trained-models-for-image-classification-with-python-code/
* Informational site for VGG16: https://medium.com/@roshankg96/transfer-learning-and-fine-tuning-model-using-vgg-16-90b5401e1ebd
* Starter code from multiple in-class assignments
* Multiple Stack Overflow pages for error research
* Multiple ChatGPT searches for partial code and error research
* TA assistance from A Carpenter and J Torres


