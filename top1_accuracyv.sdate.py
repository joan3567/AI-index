#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.read_csv("imagenet.csv", header=0, sep=",")
df = df.sort_values(by=["Date"], ascending=False).reset_index()
df1 = df[["Rank", "Top 1 Accuracy", "Date"]]


# In[2]:


top1_accuracy = []
for i in range(df.shape[0]):
    new_acc = df.loc[i,"Top 1 Accuracy"].split('%')[0]
    top1_accuracy.append(new_acc)
df['top1_accuracy'] = np.array(top1_accuracy)
df = df.sort_values(by="Date", ascending=True)


# In[3]:


#Choose the data with and without extra training data
df_extra = df[df['Other dataset'] == True]
df_no_extra = df[df['Other dataset'] == False]


# In[4]:


#Sort the and find the max accuracy for each data
df_extra_bydates = df_extra.groupby('Date').max().sort_values(by="Date", ascending=True).reset_index()
df_no_extra_bydates = df_no_extra.groupby('Date').max().sort_values(by="Date", ascending=True).reset_index()


# In[5]:


#Only keep track fo points that the accuracy is higher than the previous one
keep_indices_extra = []
acc_list_extra = []
acc = 0
idx = 0
for i in range(df_extra_bydates.shape[0]):
    new_acc = float(df_extra_bydates.loc[i,"top1_accuracy"])
    if new_acc > acc:
        keep_indices_extra.append(i)
        acc_list_extra.append(new_acc)
        acc = new_acc
        idx = i


# In[6]:


#Only keep track fo points that the accuracy is higher than the previous one
keep_indices_noextra = []
acc_list_noextra = []
acc = 0
idx = 0
for i in range(df_no_extra_bydates.shape[0]):
    new_acc = float(df_no_extra_bydates.loc[i,"top1_accuracy"])
    if new_acc > acc:
        keep_indices_noextra.append(i)
        acc_list_noextra.append(new_acc)
        acc = new_acc
        idx = i


# In[7]:


top_df_extra = df_extra_bydates.iloc[list(keep_indices_extra)].sort_values(by="Date", ascending=False)

top_df_noextra = df_no_extra_bydates.iloc[list(keep_indices_noextra)].sort_values(by="Date", ascending=False)


# In[8]:


top_df_extra


# In[11]:


top_df_extra.to_csv("accuracy_to_plot_extra3.csv", index=False)


# In[10]:


top_df_noextra.to_csv("accuracy_to_plot_noextra.csv", index=False)


# In[ ]:




