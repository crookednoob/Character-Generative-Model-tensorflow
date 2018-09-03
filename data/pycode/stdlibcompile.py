
# coding: utf-8

# In[1]:


import sys
sys.path


# In[2]:


import os

STDLIBLOC= "C:\\ProgramData\\Anaconda3\\lib"

max_files=100
count=0
with open("input.txt", "a", encoding="utf-8") as input_f:
    for path, directories, files in os.walk(STDLIBLOC):
        for file in files:
            count+=1
            if count> max_files:
                break
            elif ".py" in file:
                try:
                    with open(os.path.join(path, file), "r") as data_f:
                        contents=data_f.read()
                    input_f.write(contents)
                    input_f.write('\n')
                except Exception as e:
                    print(str(e))
                    

