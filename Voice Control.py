#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr


# In[3]:


r = sr.Recognizer()


# In[17]:


with sr.Microphone() as source:
    print('start Saying !!')
    audio = r.listen(source)
print('Speech Done..')


# In[18]:


type(audio)


# In[19]:


audio


# In[20]:


audio.frame_data


# In[22]:


data = r.recognize_google(audio)


# In[23]:


data


# In[ ]:




