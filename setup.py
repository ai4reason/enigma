from setuptools import setup, find_packages

setup(name='enigma',
      version='0.1',
      description='Enigma: Inference Guiding Machine',
      url='http://github.com/ai4reason/enigma',
      author='ai4reason',
      license='GPL3',
      packages=find_packages(),
      scripts=[
         'bin/eprover',
         'bin/enigma-features',
         'bin/train',
         'bin/predict'
      ],
      install_requires=[
         'xgboost',
         'atpy @ https://github.com/ai4reason/atpy.git'
      ],
      zip_safe=False)

