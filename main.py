
# coding: utf-8

# In[21]:


import func
import json
import sys
import os

mypath = input()


def main(mypath):
    temp=[]
    filelist=os.listdir(mypath)
    for i in filelist:
        path=mypath+'/'+i
        content = i.replace('.txt', '').split('~')
        id_info = content[0]
        artist_info = content[1]
        title_info = content[2]
        value={}
        value['ID']=id_info
        value['artist'] = artist_info 
        value['title']= title_info
        value['kid_safe']= func.kid_safe(path) 
        value['love']=func.love_test(path)
        value['mood']= func.mood_test(path) 
        value['length']= func.length_test(path) 
        value['complexity']= func.complexity(path)
        final_result=temp.append(value)
    finalresult={'characterizations':temp}
    print(json.dump(finalresult, sys.stdout, indent=4))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser('Lyrics Test')
    parser.add_argument('path', help='Path to the Lyrcis folder')
    args = parser.parse_args() 
    
    main(args.path)

