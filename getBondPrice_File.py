#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    periods = m * ppy
    coupon = face * couponRate / ppy
    discount_factors = (1 + y / ppy) ** -np.arange(1, periods + 1)
    bond_price = np.sum(coupon * discount_factors) + face * (1 + y / ppy) ** -periods
    return bond_price


# In[ ]:




