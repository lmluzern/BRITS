# Description
The source codes of RITS-I, RITS, BRITS-I, BRITS for health-care data imputation/classification

Note that Python 2 is required, I used Python 2.7.17. I had to install several packages first.

Here are the arguments I used to reproduce the experiment:

python2 main.py --epochs 1000 --batch_size 64 --model brits

python2 main.py --epochs 1000 --batch_size 64 --model rits

python2 main.py --epochs 1000 --batch_size 64 --model brits_i

python2 main.py --epochs 1000 --batch_size 64 --model rits_i
