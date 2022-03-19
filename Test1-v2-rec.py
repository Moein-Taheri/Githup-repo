#!/usr/bin/env python
# coding: utf-8

# In[1]:


import shutil
import os


# In[2]:


src_path = 'e:\\test1'


# In[3]:


dest_path = 'f:\\test1'


# In[33]:


def recurvsive_copy(src_path,dest_path):
    print(f'Creating destination directory: {dest_path}')
    os.mkdir(dest_path)
    for item in os.listdir(src_path):
        item_normal = os.path.join(src_path,item)
        # check if item_normal is a direcroty
        if os.path.isdir(item_normal):
            print(f'dir identified called recursive function on ({item_normal})')
            recurvsive_copy(item_normal,os.path.join(dest_path,item))
        # take action if item_normal is a file
        else:
            print(f'Copying file {item_normal} to {dest_path}')
            shutil.copy(item_normal,dest_path)


# In[38]:


try:
    recurvsive_copy(src_path,dest_path)
except Exception as e:
    print(f'File already existed {str(e)}')


# In[ ]:




