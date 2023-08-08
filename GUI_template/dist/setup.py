#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages

setup(
    name='PetEmotionPredictor',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'tensorflow',  # Include any other dependencies your app needs
    ],
    entry_points={
        'console_scripts': [
            'pet_emotion_predictor = your_module_name:main_function',  # Replace with your main function
        ],
    },
)

