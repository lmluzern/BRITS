# Description
The source codes of RITS-I, RITS, BRITS-I, BRITS for health-care data imputation/classification

## Requirements
Note that Python 2 is required, I used Python 2.7.17. I had to install several packages first.

  * pip2 install torch torchvision
  * pip2 install pandas
  * pip2 install ujson
  * pip2 install ipdb
  * pip2 install scikit-learn
  
(no guarantee for completeness)

## Usage

### Run BRITS On Univariate Time Series
I extracted the first column of the airq_normal.txt from https://github.com/eXascaleInfolab/bench-vldb20/tree/master/Datasets as a univariate time series (see json/json). 

Here are the arguments to run BRITS on univariate time series:

python2 main.py --epochs 1000 --batch_size 64 --model brits_i_univ

python2 main.py --epochs 1000 --batch_size 64 --model rits_i_univ

### Experiment Reproduction
Before you run the following commands, you must rename the json/json_original to json/json.

Here are the arguments I used to reproduce the experiment:

python2 main.py --epochs 1000 --batch_size 64 --model brits

python2 main.py --epochs 1000 --batch_size 64 --model rits

python2 main.py --epochs 1000 --batch_size 64 --model brits_i

python2 main.py --epochs 1000 --batch_size 64 --model rits_i
