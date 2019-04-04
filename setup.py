from setuptools import setup, find_packages

setup(name='enigma',
      version='0.1',
      description='Enigma: Efficient kNowlegde-base Inference Guiding MAchine',
      url='http://github.com/ai4reason/enigma',
      author='ai4reason',
      license='GPL3',
      packages=find_packages(),
      scripts=[
         'bin/train',
         'bin/predict',
         'bin/enigma-features'
      ],
      zip_safe=False)

