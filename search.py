import os, filecmp

def search(put, box_file):
    for i in os.listdir(put):
        if os.path.isfile(f'{put}/{i}'):
            box_file.append(f'{put}/{i}')
        if os.path.isdir(f'{put}/{i}'):
            search(f'{put}/{i}', box_file)
    return box_file


#print(f'{box_file_put1}\n{box_file_put2}')
def func():
    box_file_put1 =  search('path/to/file', [])   
    box_file_put2 = search('/path/to/file2', [])
    for i in range(-1,len(box_file_put1)-1):
        for a in range(-1,len(box_file_put2)-1):
            
            if filecmp.cmp(box_file_put1[i], box_file_put2[a], shallow=False):
                print(box_file_put1.pop(i))
                print(box_file_put2.pop(a))
        else:
            boxfile_put1 = box_file_put1[i:]
            box_file_put2 = box_file_put2[a:]
                        
    return box_file_put1, box_file_put2
            
                
                
                    
                
print(func())