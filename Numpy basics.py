#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([[1,2,3,4],[4,5,6,7]], dtype='int16') #nesting list within a list


# In[3]:


a


# In[4]:


#get dimensions
a.ndim


# In[5]:


#get shape
a.shape


# In[6]:


# get type
a.dtype


# In[7]:


#get size
a.itemsize


# # Accessing/Changing  specific elements,rows,columns,etc

# In[8]:


a = np.array([[1,2,3,4,5,6,7],[7,8,9,0,98,7,6]])


# In[9]:


a


# In[10]:


# get a specific element [r,c]
a[1,4]


# In[11]:


#get a specific row 
a[0,:]


# In[12]:


# get a specific column
a[:,2]


# In[13]:


#getting more fancy [startindex:endindex:stepsize]
a[1, 0:5:2]


# In[14]:


#to change a value
a[:,2]=[-1,-1]


# In[15]:


a


# In[16]:


#3d example
b= np.array([[[1,2],[3,4]],[[5,6],[7,8]]])


# In[17]:


print(b)


# In[18]:


#get specific element (work outside in)
b[1,0,1]


# In[19]:


b[:,0,:] = ([9,9],[9,9])


# In[20]:


b


# 
# # Initializing different types of arrays

# In[21]:


#all zeros matrix
np.zeros((1,3))


# In[22]:


#all ones matrix
np.ones((2,3), dtype='int')


# In[23]:


#any other number
np.full((2,3),2000)


# In[24]:


#random decimal numbers
np.random.rand(4,2)


# In[25]:


#random integer values
np.random.rand(4,3)


# In[26]:


#get a matrix below a certain number using random such as from 6-9
np.random.randint(6,9,size=(4,4))


# In[27]:


#the identity matrix
np.identity(7)


# In[28]:


#repeat an array
arr = np.array([[1,2,3]])
arr = np.repeat(arr,3,axis=0)
print(arr)


# In[29]:


output = np.ones((5,5))
print (output)
z= np.zeros((3,3))
z[1,1]=9
print(z)
output[1:-1,1:-1]=z
print(output)


# In[30]:


#be careful when copying arrays


# In[31]:


k = np.array([1,2,3])
b = k.copy()
b[0] = 4
print(b)


# # Mathematics 

# In[32]:


a = np.array([1,2,3,4])


# ## 

# In[33]:


a+2 #a+=2


# In[34]:


a/2


# In[35]:


a*4


# In[36]:


b = np.array([3,4,5,6])


# In[37]:


a+b


# In[38]:


a**2


# In[39]:


#take the sin
np.sin(a)


# # Linear Algebra

# In[40]:


a = np.ones([2,3])
print(a)

b=np.full([3,2],2)
print(b)


# In[41]:


#matrixmultiply 
np.matmul(a,b)


# In[42]:


#find the determinant 
c = np.identity(3)
np.linalg.det(c)


# # Statistics 

# In[43]:


stats = np.array([[1,2,3,4],[5,6,7,8]])


# In[44]:


np.min(stats)


# In[45]:


np.max(stats)


# In[46]:


np.sum(stats)


# In[47]:


np.sum(stats,axis=0)


# # Reorganizing arrays

# In[48]:


before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)


# In[49]:


after = before.reshape(8,1)
print(after)


# In[50]:


#vertically stacking vectors(making part of the same matrix)
v1= np.array([1,2,3,4])
v2= np.array([2,3,4,5])
v3 = np.array([7,8,9,10])
np.vstack([v1,v2,v3])


# In[51]:


#horizontally stacking vectors(making part of the same matrix)
h1= np.array([1,2,3,4])
h2= np.array([2,3,4,5])
h3 = np.array([7,8,9,10])
np.hstack([v1,v2,v3])


# # Miscellaneous

# In[52]:


#load data from a file
np.genfromtxt('data.txt',delimiter=',')


# In[ ]:


#advanced indexing and boolean masking


# In[ ]:


filedata = np.array([3,5,55,6,7,8,9,51,99,77,44])
filedata > 50


# In[ ]:


filedata[(filedata>50)]


# In[ ]:


## you can index with a list in NumPY
a= np.array((1,2,3,4,5,6,7,8,9))
a[[1,2,8]]


# In[ ]:


np.any(filedata>50, axis=0)


# In[ ]:




