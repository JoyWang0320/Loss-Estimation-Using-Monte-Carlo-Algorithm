## Monte Carlo Algorithm_Loss Estimation
### Problem
You run a company with two industrial plants. Occasionally there are accidents, which incur a cost.

The **csv file (accidents.csv)** contains recorded accidents over the last 4 years. The 1st column indicates where it happened (plant A or plant B). The 2nd column indicates the day (0 is 4 years ago). The 3rd column indicates the loss caused by the accidents in dollars.

(1)	Without any simulation from the data, what is the average number of accidents per year in plant A/B? What is the average loss per accident in plant A/B? What is the average loss in total per year in plan A/B?

(2)	Now assume the time interval between accidents is exponential and the natural log of a loss due to a single accident is a Guassian (aka the loss is lognormal). Implement a simulate once that simulates one year of losses for both plants.
Running simulate many, what is the average yearly loss with a relative precision of 10%? Report the bootstrap errors. 
How much should the company budget to make sure that it can cover these losses in 90% of the simulated scenarios?

### Code
I am using Python 2 and **code.py** contains the code used to solve this problem. And I import **nlib.py** (Prof. Massimo Di Pierro from DePaul University) into code.py.
### Final Report
**Final report** explains the problem, solution with explanations, and includes an appendix containing the code (commented and indented). 
