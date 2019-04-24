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
         'atpy==dev @ https://github.com/ai4reason/atpy/tarball/master#egg=atpy-dev'
      ],
      zip_safe=False)

