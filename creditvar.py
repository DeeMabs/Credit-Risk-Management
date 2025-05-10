#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
# Parametersnp.random.seed(42)
time_intervals = 10 # Simulating for 10 time intervals (e.g., hours)
initial_cash = 10000 # Initial cash balance
inflows = np.random.uniform(500, 1500, size=time_intervals) # Random inflows
outflows = np.random.uniform(700, 2000, size=time_intervals) # Random outflows
# Simulate cash balance over time
cash_balance = [initial_cash]
for inflow, outflow in zip(inflows, outflows):    
    new_balance = cash_balance[-1] + inflow - outflow
cash_balance.append(new_balance)
# Plotting the results
plt.plot(cash_balance, marker='o')
plt.title('Intra-day Liquidity Simulation')
plt.xlabel('Time Intervals')
plt.ylabel('Cash Balance')
plt.xticks(range(time_intervals + 1))
plt.grid()
plt.show()


# In[7]:


import matplotlib.pyplot as plt
# Parameters
np.random.seed(42)
initial_investment = 10000
num_simulations = 1000
num_years = 10
annual_return_mean = 0.05
annual_return_std = 0.1# Simulate portfolio values
simulated_portfolios = []
for _ in range(num_simulations):
    annual_returns = np.random.normal(annual_return_mean, annual_return_std, num_years)
portfolio_value = initial_investment * np.prod(1 + annual_returns)
simulated_portfolios.append(portfolio_value)
# Plotting the results
plt.hist(simulated_portfolios, bins=30, alpha=0.75)
plt.title('Monte Carlo Simulation of Portfolio Value')
plt.xlabel('Final Portfolio Value')
plt.ylabel('Frequency')
plt.grid()
plt.show()


# In[11]:


import numpy as np
import matplotlib.pyplot as plt
# Parameters
np.random.seed(42)
lambda_rate = 5 # Average number of arrivals per hour
time_period = 1 # One hour
num_simulations = 1000
# Simulate arrivals
arrivals = np.random.poisson(lambda_rate * time_period, num_simulations)
# Plotting the results
plt.hist(arrivals, bins=range(max(arrivals) + 1), alpha=0.75, align='left')
plt.title('Poisson Process: Customer Arrivals')
plt.xlabel('Number of Arrivals')
plt.ylabel('Frequency')
plt.xticks(range(max(arrivals) + 1));plt.grid()
plt.show()


# In[35]:





# In[ ]:





# In[5]:


import numpy as np
import matplotlib.pyplot as plt
# Parametersnp.random.seed(42)
time_intervals = 10 # Simulating for 10 time intervals (e.g., hours)
initial_cash = 10000 # Initial cash balance
inflows = np.random.uniform(500, 1500, size=time_intervals) # Random inflows
outflows = np.random.uniform(700, 2000, size=time_intervals) # Random outflows
# Simulate cash balance over time
cash_balance = [initial_cash]
for inflow, outflow in zip(inflows, outflows):    
    new_balance = cash_balance[-1] + inflow - outflow
cash_balance.append(new_balance)
# Plotting the results
plt.plot(cash_balance, marker='o')
plt.title('Intra-day Liquidity Simulation')
plt.xlabel('Time Intervals')
plt.ylabel('Cash Balance')
plt.xticks(range(time_intervals + 1))
plt.grid()
plt.show()


# In[5]:


import numpy as np
import matplotlib.pyplot as plt
# Parametersnp.random.seed(42)
time_intervals = 10 # Simulating for 10 time intervals (e.g., hours)
initial_cash = 10000 # Initial cash balance
inflows = np.random.uniform(500, 1500, size=time_intervals) # Random inflows
outflows = np.random.uniform(700, 2000, size=time_intervals) # Random outflows
# Simulate cash balance over time
cash_balance = [initial_cash]
for inflow, outflow in zip(inflows, outflows):    
    new_balance = cash_balance[-1] + inflow - outflow
cash_balance.append(new_balance)
# Plotting the results
plt.plot(cash_balance, marker='o')
plt.title('Intra-day Liquidity Simulation')
plt.xlabel('Time Intervals')
plt.ylabel('Cash Balance')
plt.xticks(range(time_intervals + 1))
plt.grid()
plt.show()




# In[41]:


import numpy as np
import matplotlib.pyplot as plt
# Parametersnp.random.seed(42)
time_intervals = 10 # Simulating for 10 time intervals (e.g., hours)
initial_cash = 10000 # Initial cash balance
inflows = np.random.uniform(500, 1500, size=time_intervals) # Random inflows
outflows = np.random.uniform(700, 2000, size=time_intervals) # Random outflows
# Simulate cash balance over time
cash_balance = [initial_cash]
for inflow, outflow in zip(inflows, outflows):    
    new_balance = cash_balance[-1] + inflow - outflow
cash_balance.append(new_balance)
# Plotting the results
plt.plot(cash_balance, marker='o')
plt.title('Intra-day Liquidity Simulation')
plt.xlabel('Time Intervals')
plt.ylabel('Cash Balance')
plt.xticks(range(time_intervals + 1))
plt.grid()
plt.show()

import matplotlib.pyplot as plt
# Parameters
np.random.seed(42)
initial_investment = 10000
num_simulations = 1000
num_years = 10
annual_return_mean = 0.05
annual_return_std = 0.1# Simulate portfolio values
simulated_portfolios = []
for _ in range(num_simulations):
    annual_returns = np.random.normal(annual_return_mean, annual_return_std, num_years)
portfolio_value = initial_investment * np.prod(1 + annual_returns)
simulated_portfolios.append(portfolio_value)
# Plotting the results
plt.hist(simulated_portfolios, bins=30, alpha=0.75)
plt.title('Monte Carlo Simulation of Portfolio Value')
plt.xlabel('Final Portfolio Value')
plt.ylabel('Frequency')
plt.grid()
plt.show()



import numpy as np
import matplotlib.pyplot as plt
# Parameters
np.random.seed(42)
lambda_rate = 5 # Average number of arrivals per hour
time_period = 1 # One hour
num_simulations = 1000
# Simulate arrivals
arrivals = np.random.poisson(lambda_rate * time_period, num_simulations)
# Plotting the results
plt.hist(arrivals, bins=range(max(arrivals) + 1), alpha=0.75, align='left')
plt.title('Poisson Process: Customer Arrivals')
plt.xlabel('Number of Arrivals')
plt.ylabel('Frequency')
plt.xticks(range(max(arrivals) + 1))
plt.grid()
plt.show()


# In[ ]:




