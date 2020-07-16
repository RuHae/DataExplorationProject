# DataExplorationProject

## Which Version
Python 3.8

## Differences

GPU Support

Code adjustments to support Tensorflow 2.0 and Python 3.8

# Setup

## Create the virtual python environment

copy in your shell:
	` python -m venv <name_of_your_env> ` 
	
## Start the virtual env

copy in your shell:
   For Windows: ` <name_of_your_env>\Scripts\activate.bat ` 
	
   For Linux / MacOS: ` source <name_of_your_env>/bin/activate `
	
## Install requirements.txt 

The requirements.txt is in the git.
copy to your shell after you started the virtual env:
	` pip install -r requirements4.txt `  
## Start preprocessing
Uncomment the following line in run.py
	` #load_training_images("..\\breast-histopathology-images\\IDC_regular_ps50_idx5") `

Run the in your shell (make sure you are in the correct directory:
	` python run.py `
	
### Credits

https://pip.pypa.io/en/stable/reference/pip_install/

https://docs.python.org/3/tutorial/venv.html



# DataExploration
