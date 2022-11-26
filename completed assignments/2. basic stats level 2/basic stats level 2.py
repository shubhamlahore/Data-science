#!/usr/bin/env python
# coding: utf-8

# # Assignment-2 (Set-1)

# #### Question - 1

# In[4]:


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df=pd.DataFrame(data={'Name of the company':['Allied Signal','Bankers Trust','General Mills','ITT Industries','J.P.Morgan & Co.','Lehman Brothers','Marriott','MCI','Merrill Lynch','Microsoft','Morgan Stanley','Sun Microsystems','Travelers','US Airways','Warner-Lambert'],'Measure X':[24.23, 25.53, 25.41, 24.14, 29.62, 28.25, 25.81, 24.39, 40.26, 32.95, 91.36, 25.99, 39.42, 26.71, 35.00]})


# In[8]:


df


# In[9]:


df.mean()


# In[10]:


df.var()


# In[11]:


df.std()


# In[12]:


plt.boxplot(df['Measure X'])


# In[13]:


plt.figure(figsize=(6,8))
plt.pie(df['Measure X'],autopct='%1.0f%%',labels=df['Name of the company'])
plt.show()


# # Assignment-2 (Set-2)

# #### Question - 1

# In[14]:


import pandas as pd
from scipy import stats


# In[15]:


1-stats.norm.cdf(0.625)


# #### Question - 2

# In[16]:


# A. More employees at the processing center are older than 44 than between 38 and 44.

# p(X>44); Employees older than 44 yrs of age
1-stats.norm.cdf(44,loc=38,scale=6)


# In[17]:


# p(38<X<44); Employees between 38 to 44 yrs of age
stats.norm.cdf(44,38,6)-stats.norm.cdf(38,38,6)


# In[18]:


# B. A training program for employees under the age of 30 at the center would be expected to attract about 36 employees.

# P(X<30); Employees under 30 yrs of age
stats.norm.cdf(30,38,6)


# In[19]:


# No. of employees attending training program from 400 nos. is N*P(X<30)
400*stats.norm.cdf(30,38,6)


# #### Question - 4

# In[20]:


stats.norm.interval(0.99,100,20)


# #### Question - 5

# In[21]:


# Mean profits from two different divisions of a company = Mean1 + Mean2
Mean = 5+7
print('Mean Profit is Rs', Mean*45,'Million')


# In[22]:


# Variance of profits from two different divisions of a company = SD^2 = SD1^2 + SD2^2
SD = np.sqrt((9)+(16))
print('Standard Deviation is Rs', SD*45, 'Million')


# In[23]:


# A. Specify a Rupee range (centered on the mean) such that it contains 95% probability for the annual profit of the company.
print('Range is Rs',(stats.norm.interval(0.95,540,225)),'in Millions')


# In[24]:


# B. Specify the 5th percentile of profit (in Rupees) for the company
# To compute 5th Percentile, we use the formula X=μ + Zσ; wherein from z table, 5 percentile = -1.645
X= 540+(-1.645)*(225)
print('5th percentile of profit (in Million Rupees) is',np.round(X,))


# In[25]:


# C. Which of the two divisions has a larger probability of making a loss in a given year?

# Probability of Division 1 making a loss P(X<0)
stats.norm.cdf(0,5,3)


# In[26]:


# Probability of Division 2 making a loss P(X<0)
stats.norm.cdf(0,7,4)


# # Assignment-2 (Set-3)¶

# #### Question - 5(i)

# In[28]:


# Apply One-Sample One-Tail z-test
z_scores=(0.046-0.05)/(np.sqrt((0.05*(1-0.05))/2000))
z_scores


# #### Question - 5(ii)

# In[29]:


# Find Probability assuming null hyposthesis, so as to compare with Type-1 error α = 0.05
p_value=1-stats.norm.cdf(abs(z_scores))
p_value


# In[30]:


stats.t.ppf(0.954,2000)


# # Assignment-2 (Set-4)

# #### Question - 4

# In[31]:


x_bar = 45
s_std = 40
mew = 50

t = np.round(stats.t.ppf(0.025, df = 249),2)
t

# t_value = (x_bar - mew)/(sample_std/n**0.5)
# t = 45-50 or z = 55-50 z = +/- 5

# t = 5/(40/n**0.5)
# n = (sample_standard_deviation*tscore)/(sample_mean=population_mean)
n = ((s_std*abs(t)) / (5))**2

print('The Auditors would like to maintain the probability of investigation to 5%, they should sample',np.round(n,),'transactions if they do not want to change the thresholds of 45 to 55')

df= n-1
print(n, df)

np.round(stats.t.interval(alpha = 0.95, df = df, loc = mew, scale = s_std/np.sqrt(n)),)

