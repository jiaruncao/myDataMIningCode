
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report


# In[4]:


malls=pd.read_csv('mall_test2.csv')#mall_test2.csv
malls=malls.mall_id.values.tolist()
#data = pd.read_csv('mySplitData/m_615.csv')


# In[3]:



malls = ['m_2058','m_1831']


# In[4]:


for mall in malls:
    data = pd.read_csv('mySplitData/'+mall+'.csv')
    test = pd.read_csv('splitTestData/'+mall+'.csv')
    wifi_infos1 = test['wifi_infos']

    list_wifi1 = []

    dict_wifi1 = {}

    for wifi_info1 in wifi_infos1:
  #  print wifi_info1
        wifi1 = wifi_info1.split(';')
        for wf1 in wifi1 :
      #  print wf1
            bssid1 = str(wf1.split('|')[0])
            signal1 = float(wf1.split('|')[1])
            dict_wifi1[bssid1]  = signal1
       # print dict_wifi1
            sorted_dict_wifi1 = sorted(dict_wifi1.items(),key=lambda x:x[1],reverse=True)
   #     print sorted_dict_wifi1
        list_wifi1.append(sorted_dict_wifi1)
        dict_wifi1 = {}
        sorted_dict_wifi1={}
    allWifi1 = []

#print list_wifi1
    for mywifi1 in list_wifi1:
        for wifi1 in mywifi1:
            allWifi1.append(wifi1[0])
#print len(allWifi1)
    allWifi1 = list(set(allWifi1))



#--------------------------------------------------------

    wifi_infos = data['wifi_infos']
    list_wifi = []
    dict_wifi = {}
    count = 0
    for wifi_info in wifi_infos:
        wifi = wifi_info.split(';')
        for wf in wifi :
            bssid = str(wf.split('|')[0])
            signal = float(wf.split('|')[1])
            dict_wifi[bssid]  = signal
            sorted_dict_wifi = sorted(dict_wifi.items(),key=lambda x:x[1],reverse=True)
        list_wifi.append(sorted_dict_wifi)
        dict_wifi = {}
        sorted_dict_wifi={}
    allWifi = []
    for mywifi in list_wifi:
        for wifi in mywifi:
            allWifi.append(wifi[0])
   # print len(allWifi)
    allWifi = list(set(allWifi).union(set(allWifi1)))
  #  print len(allWifi)
    allWifi_sorted = []
    for singleWifi in allWifi:
        singleWifi = str(singleWifi).strip('b')
        singleWifi = str(singleWifi).strip('_')
        singleWifi = int(singleWifi)
        allWifi_sorted.append(singleWifi)
    allWifi_sorted = sorted(allWifi_sorted)
    Wifi_sorted = []
    for i in allWifi_sorted:
        i_ = 'b_' + str(i)
        Wifi_sorted.append(i_)
    wifi_matrix  = np.zeros([int(data['wifi_infos'].count()),len(allWifi_sorted)])
    counter = 0
    for wifi in list_wifi:
        for wf in wifi:
            index_wifi = Wifi_sorted.index(str(wf[0]))
            wifi_matrix[counter,index_wifi] = int(wf[1])
        counter += 1

    
    wifi_matrix1  = np.zeros([int(test['row_id'].count()),len(allWifi_sorted)])
    counter1 = 0
    for wifi1 in list_wifi1:
        for wf1 in wifi1:
     #   print wf[1]
            index_wifi1 = Wifi_sorted.index(str(wf1[0]))
    #    print index_wifi
            wifi_matrix1[counter1,index_wifi1] = int(wf1[1])
        counter1 += 1
    label = list(data['shop_id'])
    knn = KNeighborsClassifier()

    k_range = list(range(1,20))
#weight_options = ['uniform','distance']
       # algorithm_options = ['auto','ball_tree','kd_tree','brute']
    param_gridknn = dict(n_neighbors = k_range)
    gridKNN = GridSearchCV(knn,param_gridknn,cv=3,scoring='accuracy',verbose=1,error_score= 0,n_jobs=-1)
    gridKNN.fit(wifi_matrix,label)
    fr = open('knn_wifi_Parameter.txt','a')
    fr.write(str(mall)+'\n')
    fr.write(str(gridKNN.best_params_)+'\n')
    fr.write('\n')
    fr.close()
    predict = gridKNN.predict(wifi_matrix1)
    predict = pd.DataFrame(predict,columns=['shop_id'])
    pre_result = pd.concat([test['row_id'],predict['shop_id']],axis = 1)
    result = pd.DataFrame(columns=['row_id','shop_id'])
    result = pd.concat([result,pre_result],axis = 0)
    print mall
    result.to_csv('resuat_'+mall+'.csv',index=None)
#result.to_csv('result.csv',index = 0)


# In[ ]:





# In[ ]:





# In[124]:





# In[126]:





# In[127]:





# In[161]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[189]:





# In[191]:





# In[195]:





# In[196]:





# In[197]:





# In[198]:





# In[ ]:




