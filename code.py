
# load data

import csv
from nlib import *

plant_dic = {'A':[],'B':[]}
with open('accidents.csv') as myfile:
    reader = csv.reader(myfile)
    for row in reader:
        plant_dic[row[0]].append([row[1],row[2]])
        
#-------------------------------------------------------
        
# basic info of two plants

A_annual_acc = 0
A_annual_loss = 0
B_annual_acc = 0
B_annual_loss = 0
A_time_lst = []
B_time_lst = []
A_annual_loss_lst = []
B_annual_loss_lst = []

for i in plant_dic['A']:
    day = eval(i[0]) 
    loss = eval(i[1])
    A_annual_acc +=1
    A_time_lst.append(day)
    A_annual_loss += loss
    A_annual_loss_lst.append(loss)

for i in plant_dic['B']:
    day = eval(i[0]) 
    loss = eval(i[1])
    B_annual_acc +=1
    B_time_lst.append(day)
    B_annual_loss += loss
    B_annual_loss_lst.append(loss)
    
print 'The average number of accidents per year in plant A = {}'.format(round(float(A_annual_acc)/4,4))
print 'The average number of accidents per year in plant B = {}'.format(round(float(B_annual_acc)/4,4))
print 'The average loss per accident in plant A = {}'.format(round(float(A_annual_loss)/A_annual_acc,4))
print 'The average loss per accident in plant B = {}'.format(round(float(B_annual_loss)/B_annual_acc,4))
print 'The average loss in total per year in plan A = {}'.format(round(float(A_annual_loss)/4,4))
print 'The average loss in total per year in plan B = {}'.format(round(float(B_annual_loss)/4,4))
print('------------------------------------------------------------------------------------')

# distribution of time interval in 2 plants

A_interval_lst = []
for i in range(len(A_time_lst)-1):
    interval = A_time_lst[i+1]-A_time_lst[i]
    A_interval_lst.append(interval)

B_interval_lst = []
for i in range(len(B_time_lst)-1):
    interval = B_time_lst[i+1]-B_time_lst[i]
    B_interval_lst.append(interval)
    
#Canvas().hist(A_interval_lst).save('A_time.png')  #plot the time interval in plant A
#Canvas().hist(B_interval_lst).save('B_time.png')  #plot the time interval in plant B

# distribution of loss in 2 plants

import math

A_log_lst = []
for loss in A_annual_loss_lst:
    log_loss = math.log(loss)
    A_log_lst.append(log_loss)

B_log_lst = []
for loss in B_annual_loss_lst:
    log_loss = math.log(loss)
    B_log_lst.append(log_loss)
    
A_mu = mean(A_log_lst)
A_sigma = sd(A_log_lst)
B_mu = mean(B_log_lst)
B_sigma = sd(B_log_lst)

#Canvas().hist(A_annual_loss_lst).save('A_loss_dis.png')  #plot the loss in plant A
#Canvas().hist(A_log_lst).save('A_log_loss_dis.png')      #plot the log loss in plant A
#Canvas().hist(B_annual_loss_lst).save('B_loss_dis.png')  #plot the loss in plant B
#Canvas().hist(B_log_lst).save('B_log_loss_dis.png')      #plot the log loss in plant B
print round(A_mu,4), round(A_sigma,4)
print round(B_mu,4), round(B_sigma,4)
print('-----------------------------------------------------------------------------------')
  
# simulation

import random

class OptionLoss(MCEngine):
    
    def __init__(self):
        pass
        
    def simulate_once(self):
        t_A = 0
        t_B = 0
        max_time = 1   # simulate 1 year
        lamb_A = 33.75 # the number of event per year
        lamb_B = 39.0
        loss_A = 0
        loss_B = 0
        self.A_loss = []
        self.B_loss = []
        self.A_time = []
        self.B_time = []
            
        while True:
            t_A = t_A + random.expovariate(lamb_A)
            if t_A > max_time: break
            self.A_time.append(int(t_A*365))
            log_loss = random.gauss(A_mu, A_sigma)
            loss_A = loss_A + math.exp(log_loss)
            self.A_loss.append(loss_A)
      
        while True:
            t_B = t_B + random.expovariate(lamb_B)
            if t_B > max_time: break
            self.B_time.append(int(t_B*365))
            log_loss = random.gauss(B_mu, B_sigma)
            loss_B = loss_B + math.exp(log_loss)
            self.B_loss.append(loss_B)
        
        return loss_A + loss_B

OL = OptionLoss()
mu_minus, mu, mu_plus = OL.simulate_many(ap=0.1,rp=0.1,ns=1000)
print 'confidence interval(at %i%%) is %f, %f, %f' % (90, mu_minus, mu, mu_plus)

# plot and distribution

loss = []
for i in range(100):
    loss.append(OL.simulate_once())
Canvas().hist(loss).save('loss.png')

A_data = []
for i in range(len(OL.A_time)):
    A_data.append((OL.A_time[i],OL.A_loss[i]))
B_data = []
for i in range(len(OL.B_time)):
    B_data.append((OL.B_time[i],OL.B_loss[i]))

Canvas().plot(A_data).save('A_loss_graph.png')
Canvas().plot(B_data).save('B_loss_graph.png')








