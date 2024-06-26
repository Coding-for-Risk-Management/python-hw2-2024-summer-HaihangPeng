#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    periods = m * ppy
    coupon = couponRate * face / ppy
    discount_factors = np.array([(1 + y / ppy) ** -i for i in range(1, periods + 1)])
    cash_flows = np.array([coupon] * (periods - 1) + [coupon + face])
    weighted_cash_flows = cash_flows * np.arange(1, periods + 1)
    
    present_value = np.sum(cash_flows * discount_factors)
    weighted_present_value = np.sum(weighted_cash_flows * discount_factors)
    
    duration = weighted_present_value / present_value
    
    return duration


# In[ ]:




