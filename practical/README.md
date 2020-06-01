# QLS 612 Assignment
David MacDonald

## Background
This is the submisstion for QLS 612. It consists of code and text in a python notebook, myanalysis.ipynb.

## Instructions
To run the code, install the dependencies in requirements.txt. I recommend doing this in a virtual environment.
	source /path/to/venv/bin/activate

	pip install -r requirements.txt

You can then open the notebook in Jupyter:

	jupyter notebook myanalysis.ipynb

Be sure that you select the kernel associated with your virtual environment, or the dependencies may not be met.

You can then run all cells in the notebook.

## Product
The notebook will read the data file brainsize.csv, add two columns of random noise partY and partY2.

The first figure visualizes these distributions.

The second figure shows the relationship between partY and the variables in brainsize.csv.

The rest of the output consists of linear models.
