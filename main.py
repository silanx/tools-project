
# coding: utf-8

# In[ ]:


import func5
import json
import sys
import os

mypath = input()
filelist=os.listdir(mypath)

def main():
    for i in filelist:
        path=mypath+'/'+file
        content = i.replace('.txt', '').split('~')
        id_info = content[0]
        artist_info = content[1]
        title_info = content[2]
        value = {'ID': id_info ,
         'artist': artist_info, 
         'title': title_info,
         'kid_safe': func5.kid_safe(path), 
         'love': func5.love_test(path), 
         'mood': func5.mood_test(path), 
         'length': func5.length_test(path), 
         'complexity': func5.complexity(path)}
        output=json.dump(value)
    final_result=[].append(output)
    return json.dump(finalresult, sys.stdout, indent=4)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser('Lyrics Test')
    parser.add_argument('path', help='Path to the Lyrcis folder')
    args = parser.parse_args() 
    
    main(args.path)

