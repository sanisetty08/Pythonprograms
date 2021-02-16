# coding: utf-8

# In[1]:

# creating a list

marks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# In[2]:

marks

# In[3]:

marks[5]

# In[4]:

marks[0:6]

# In[5]:

# adding an element

marks.append(11)

# In[6]:

marks

# In[7]:

marks.extend([12, 13])

# In[8]:

marks

# In[9]:

marks.append([14, 15])

# In[10]:

marks

# In[11]:

# deleting elements

marks.remove([14, 15])

# In[12]:

marks

# In[13]:

del marks[0]

# In[14]:

marks

# In[15]:

# accessing list elements

for mark in marks:
    print(mark)

# In[16]:

for mark in marks:
    print(mark + 1)

# In[ ]:

sam = [45, 36, 54, 78, 44]
