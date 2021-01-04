import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
import random
from random import randint
from random import seed
from tqdm import tqdm




def transform_dict(categories_file_filtered):

    d=categories_file_filtered

    d_keys=list(string.lower() for string in d.keys())


    d_values=[value for value in d.values()]


    d={}

    i=0



    for key in d_keys:
    
    
        d[key]=d_values[i]
    
        i+=1
    
    
    return d


def categories_input(d):
    
    
    stop=False

    while stop==False:
    
        cat_1=input('insert the first category')
    
        cat_1=cat_1.lower()
    
        cat_1=re.sub(' ','_',cat_1) 
    
   
    
    
    
        cat_2=input('insert the second category')
    
        cat_2=cat_2.lower()
    
        cat_2=re.sub(' ','_',cat_2)
    
    

        if cat_1 and cat_2 in d.keys():
        
       
            try:
    
        
                all_pages=list(set(d[cat_1]).union(set(d[cat_2])))
        
                stop=True
            
            except KeyError:
            
                continue
        
        else:
        
            print('the categories you are looking for is not in the categories considered or you wrote them wrongly.')
        
            x=input('press any character if you want to continue, otherwise press a digit ')
        
            try:
            
                x=int(x)
            
                break
            
            except ValueError:
            
                continue
            
    
    return all_pages
    

def input_pages(all_pages,page_names):


    pages_dict={pag:[] for pag in all_pages}

    for page_number in all_pages:
    
    
        pages_dict[page_number]=page_names[page_number].lower()
    

    
    pages_dict_inv={value:key for key,value in pages_dict.items()}    



    flag=False


    while flag==False:
    
        try:

            start_pag=pages_dict_inv[input('insert the first page '.lower())]

            end_pag=pages_dict_inv[input('insert the second page '.lower())]
        
        
            if start_pag and end_pag in pages_dict.keys():
            
                flag=True
        
    
        except KeyError:
        
           
            print('you have to insert two pages which are in the two categories')
        
        
    return start_pag, end_pag


def out_subgraph(all_pages,out_degree,d):
    
    out_d={x:[] for x in all_pages}

    for key,value in out_degree.items():

        if key in out_d.keys():
        
            for x in value:
            
                if x in out_d.keys():
            
                   out_d[key].append(x)


    out_d=dict(sorted(out_d.items(),key=lambda x:x[0]))
    
    return out_d


def in_subgraph(all_pages,in_degree,d):
    
    in_d={x:[] for x in all_pages}

    for key,value in in_degree.items():

        if key in in_d.keys():
        
            for x in value:
            
                if x in in_d.keys():
            
                    in_d[key].append(x)
    
    
    in_d=dict(sorted(in_d.items(),key=lambda x:x[0]))
    
    return in_d


def links_distance(subgraph,start_vertex,end_vertex):

    layers={}
    
    queue=[]

    queue.append(start_vertex)

    distances={}
    
    distances[start_vertex]=0

    visited={vertex:False for vertex in subgraph.keys()}
    
    visited[start_vertex]=True

    try:
    
        if len(subgraph[start_vertex])==0:
        
            return 'the first page has no connections among the pages of the two categories considered'
    
    except KeyError:
            
        return 'the starting page is not a key in the subgraph'
        
        
    
    
    
    while not len(queue)==0:
    
        count=0
        
        vertex=queue.pop(0)
        
        
        
        
        layers[vertex]=[]
        
        
        
        for neighbour in subgraph[vertex]:
            
            
            
            
            if neighbour==end_vertex:
                
                node=list(layers.keys())[-1]
                
                nodes=[node]
                
                while node!=start_vertex:
                    
                    for key,values in layers.items():
                        
                        if node in values:
                            
                            node=key
                            
                            nodes.append(node)
                        

                return print('the minimum set of pages to be removed','\n',
                'in order to disconnect the two pages is','\n',nodes[:-1])
        
            
            
            
            
            try:
                
                
                if visited[neighbour]==False:
                
                    
                    
                    
                    visited[neighbour]=True
            
                    distances[neighbour]=distances[vertex]+1
            
                    queue.append(neighbour)
                
                    layers[vertex].append(neighbour)
                    
                    
                
                    
            
            
            except KeyError:
                
                
                count+=1
                
                if count==len(subgraph[vertex]):
                    
                    return 'it is impossible to reach from the first page the second page'
                
                
                
       
            

    return  'the starting page is connected with itself'   
            


def cat_input(d):    
    
    stop=False

    while stop==False:
    
        input_cat=input('insert a category ')
    
        input_cat=input_cat.lower()
    
        input_cat=re.sub(' ','_',input_cat)
    
        if input_cat in d.keys():
        
           stop=True
        
        else: 
        
            print('the category you are looking for is not in the categories considered or you wrote wrongly.')
        
            x=input('press any character if you want to continue, otherwise press a digit ')
        
            try:
            
                x=int(x)
            
                break
            
            except ValueError:
            
                continue
            
    return input_cat


def cat_distance(subgraph,start_vertex):

    
    
    queue=[]

    queue.append(start_vertex)

    distances={}
    
    distances[start_vertex]=0

    visited={vertex:False for vertex in subgraph.keys()}
    
    visited[start_vertex]=True

    
    try:
    
    
        if len(subgraph[start_vertex])==0:
        
            return 'not'
    
    
    
        while not len(queue)==0:
    
            count=0
        
            vertex=queue.pop(0)
        
        
        
        
       
        
        
        
            for neighbour in subgraph[vertex]:
            
            
            
            
           
            
            
                try:
                
                
                    if visited[neighbour]==False:
                
                    
                    
                    
                        visited[neighbour]=True
            
                        distances[neighbour]=distances[vertex]+1
            
                        queue.append(neighbour)
                
                    
                    
                    
                
                    
            
            
                except KeyError:
                
                
                    count+=1
                
   



    except KeyError:
        
        return('not')
                
   

    return distances 



def dictionary_distances(cat_distance,in_degree,new_lista,categories_filtered,d_cat):
    
    
    
    
    for page in tqdm(new_lista):
    
    
        d_dist=cat_distance(in_degree,page)   #in d_dist are stored the distances from the starting page.
    
    
        if type(d_dist)!=str:
    
    
            for key,value in d_dist.items():
        
                
                cat_name=categories_filtered[key]  #cat_name is the category name whereas key is the the number of the poge
        
        
        
                d_cat[cat_name].append(value)  #value is the single distance
    
    
    return d_cat
    
    

    
    
    
    
    
    
    
def median(d_cat):

    
    d_result={} #in this dictionary the key will be category name and the median will be the be the value

    for key,value in d_cat.items():
    

    
        if  len(value)!=0:
        
        
            median=np.median(value)
        
            d_result[key]=median
        
    
    return d_result 
