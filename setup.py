from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    description="Math Quiz",
    author="Constantin Wolff",
    author_email="constantin.wolff@fau.de",
    packages=find_packages(), 
    install_requires=[
        "requests", 
        "numpy"
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=dsss_homework_2.math_quiz.math_quiz:main',  
        ],
    },
)
