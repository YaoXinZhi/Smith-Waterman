
# file Smith-Waterman
# /usr/bin/python
# coding : utf-8

import numpy as np
from numpy import *
import sys 
import getopt

def compare(str1,str2):
    #socreing system 
    if str1 == str2:
        return match_score
    else :
        return mismatch_score
    
def loss_function(matrix,i,j,Label_Dir):
    
    a = matrix[i-1,j] + compare(Seq1[i-1],'-')
    b = matrix[i,j-1] + compare(Seq2[j-1],'-')
    c = matrix[i-1,j-1] + compare(Seq1[i-1],Seq2[j-1])
    save_CellLabel(i,j,a,b,c,Label_Dir)
    if max(a,b,c) < 0:
        matrix[i,j] = 0
    else:
        matrix[i,j] = max(a,b,c)
    return matrix
     
def save_CellLabel(m,n,a,b,c,matrix_to_return):
    
    position = '%s%s' % (str(m),str(n))
    matrix_to_return[position] = []
    if max(a,b,c) < 0:
        matrix_to_return[position].append('N')
    else:
        if max(a,b,c) == a:
            matrix_to_return[position].append('U')
        if max(a,b,c) == b:
            matrix_to_return[position].append('L')
        if max(a,b,c) == c:
            matrix_to_return[position].append('O')            

def generate_matrix(row,col):
    
    x = len(row)+1
    y = len(col)+1
    distance_matrix = mat(zeros((x,y)))
    Cell_Label = {}
    
    for i in range(1,x):
        for j in range(1,y):
            distance_matrix = loss_function(distance_matrix,i,j,Cell_Label)
            
    return distance_matrix , Cell_Label
    
    



def get_string(file):
    
    with open(file,'r') as f:
        for line in f:
            l = line.replace('\n','')
            if '>' in l:
                pass
            else:
                string = l
                
    return string 

def print_matrix(result):
    
    print ('socore matrix: ')
    row , col = shape(result)
    print()
    print("        ", end = '')
    for i in Seq2:
        print(i, end='\t')
    print()
    for i in range(0, row):
        if (i > 0):
            print(Seq1[i-1], end = '\t')
        else:
            print("  ", end = '')
    
        for j in range(0, col):
            print('%d' % result[i,j], end = '\t')
        print()
        
def get_OptimalPath(Scoring_matrix , Label_dir):
    #get OptimalPath base Label Matrix
    x ,y  = shape(Scoring_matrix)
    Start = {'position':[],'score' :0}
    
    # Find the starting position
    for i in range(1,x):
        for j in range(1,y):
            position = '%s%s' % (str(i),str(j))
            if Scoring_matrix[i,j] == Start['score']:
                Start['position'].append(position)
            if Scoring_matrix[i,j] > Start['score']:
                Start['position'] = [position] 
                Start['score'] = Scoring_matrix[i,j]
    
    AtoReturn = []
    BtoReturn = []
    for p in range(0,len(Start['position'])):
        location = Start['position'][p]
        row = int(location[0])
        col = int(location[1])
        new_SeqA = ''
        new_Seqb = ''
        while 1:
            if 'N' in Label_dir[location]:  
                AtoReturn.append(new_SeqA[::-1])
                BtoReturn.append(new_Seqb[::-1])
                break            
            if 'L' in Label_dir[location]:
                if len(Label_dir[location]) == 1:
                    col = col-1                
                new_SeqA = new_SeqA + '-'
                new_Seqb = new_Seqb + Seq2[col]                                
            elif 'U' in Label_dir[location]:
                if len(Label_dir[location]) == 1:
                    row = row-1                 
                new_Seqb = new_Seqb + '-'
                new_SeqA = new_SeqA + Seq1[row]                             
            elif 'O' in Label_dir[location]:
                row , col = row-1 ,col-1
                new_SeqA = new_SeqA + Seq1[row]
                new_Seqb = new_Seqb + Seq2[col]      
            if len(Label_dir[location]) > 1:
                row , col = row-1 , col-1
            location = '%s%s' % (str(row),str(col))

    return AtoReturn , BtoReturn
            
def print_result(sequenceA,sequenceB):
    print ('\n')
    print ('    Result    \n')
    print ('Sequences : ')
    print ('Sequence 1 : ' + Seq1)
    print ('Sequence 2 : ' + Seq2+'\n')
    print ('Paramenters :')
    print ('Substitution matrix :  a = b   S(a,b)= ' + str(match_score))
    print ('                       a != b  S(a,b)= ' + str(mismatch_score)+'\n')
    print ('Result: ')
    for a in range(len(sequenceA)):
        for b in range(len(sequenceB)):           
            print ('Sequence1   ' + str(sequenceA[a]))
            print ('Sequence2   ' + str(sequenceB[b]))
    
    
    
            
            
    
    


def main():
    
    Distance_matrix , Cell_Label = generate_matrix(Seq1,Seq2)
    print_matrix(Distance_matrix)
    SequenceA,SequenceB = get_OptimalPath(Distance_matrix,Cell_Label)
    print_result(SequenceA,SequenceB)
    
    
    
    
    

if __name__ == '__main__' :
    opts , args = getopt.getopt(sys.argv[1:],'h',['match=','mismatch=','file1=','file2='])
    InputFile1 = '/home/yaoxinzhi/桌面/Bioinformatics/Sequence_Alignment/Smith-Waterman/Sequence/Seq1.fasta'
    InputFile2 = '/home/yaoxinzhi/桌面/Bioinformatics/Sequence_Alignment/Smith-Waterman/Sequence/Seq2.fasta'
    match_score = 1
    mismatch_score = -1
    
    for op , value in opts:
        if op == '--file1':
            InputFile1 = value
        elif op == '--file2':
            InputFile2 = value
        elif op == '--match':
            match_score = float(value)
        elif op == '--mismatch':
            mismatch_score = float(value)
            
    Seq1 = get_string(InputFile1)
    Seq2 = get_string (InputFile2)
    print ('matrix shape: '+str(len(Seq1))+'*'+str(len(Seq2)))
    main()

