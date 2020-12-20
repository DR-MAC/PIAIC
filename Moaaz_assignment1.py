#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a = np.zeros(5)


# In[2]:


a


# In[3]:


a.dtype


# In[4]:


b = np.ones(5)
b


# In[5]:


l = [1, 2, 3, 4, 5]
c = np.array(l)
c


# In[6]:


c.shape


# In[7]:


d = np.empty([4,4])
d


# In[8]:


e = np.arange(1, 20, 4)
e


# In[10]:


e.size


# In[12]:


e.shape


# In[14]:


x = [4, 9, 16, 25]
y = np.sqrt(x)
y


# In[15]:


z = np.power(x, 2)
z


# In[16]:


np.eye((5))


# In[17]:


a = np.diag([2, 4, 8])
a 


# In[18]:


result = np.array([15, 20, 24, 28, 32, 40, 48, 50])
np.where(result>25, "PASS", "FAIL")


# In[19]:


a = np.linspace(1, 5, 5)
a


# In[20]:


x = np.sin(np.pi/2)
x


# In[21]:


y = np.cos(np.pi/2)
y


# In[23]:


x = np.lcm(15, 30)
x


# In[24]:


y = np.gcd(30, 6)
y 


# In[27]:


z = np.prod([x, y])
z


# In[28]:


x = np.array([1, 2, 2, 3, 4, 5, 6, 6, 7])
y = np.unique(x)
y


# In[29]:


z = x.max()
z


# In[30]:


x.min()


# In[32]:


a = np.array([[2, 4],[6, 3]])
np.sort(a)


# In[34]:


x2 = np.arange(4, 12)
x2


# In[35]:


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
x = np.dot(a, b)
x


# In[36]:


x = np.arange(12).reshape(3,4)
x


# In[38]:


x.sum(axis = 0)


# In[39]:


x.sum(axis = 1)


# In[40]:


a = np.array([1, 2, 3, 4, 5, 6])
a.mean()


# In[41]:


a.sum()


# In[42]:


a.cumsum()


# In[43]:


a.prod()


# In[44]:


a.cumprod()


# In[45]:


a>3


# In[46]:


a<4


# In[49]:


x = np.random.randn(2, 3)
y = np.random.randn(3, 2)


# In[51]:


a = x.dot(y)
a


# In[52]:


a.transpose()


# In[54]:


x = np.array([[2,1,1], [4, 2, 1], [2,1,1]]) 
y = np.linalg.det(x) 
y


# In[55]:


x.trace()


# In[56]:


x.any()


# In[57]:


x.all()


# In[59]:


a = np.array([[0, 2, 6, 0],
              [1, 0, 2, 0]])
b = np.count_nonzero(a)
b


# In[60]:


c = np.count_nonzero(a, axis=0)
c


# In[61]:


a = np.arange(9).reshape(3,3)
a


# In[62]:


b = a[[1, 0, 2], :]
b


# In[64]:


c = a[:, : : -1]
c


# In[ ]:




