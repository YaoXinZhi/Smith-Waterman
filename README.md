The Smith–Waterman algorithm performs local sequence alignment; that is, for determining similar regions between two strings of nucleic acid sequences or protein sequences. Instead of looking at the entire sequence, the Smith–Waterman algorithm compares segments of all possible lengths and optimizes the similarity measure.

In other words, this algorithm is an improvement of the application of the Needleman-Wunsch algorithm in bioinformatics, which is different from the original algorithm:

1.First, in the initialization phase, the first row and the first column are fully padded with 0 (and the pointers for the first row and first column are all empty).

2.Second, when filling a table, if a score is negative, then 0 is used instead, and only the return pointer is added to the cell with a positive score.

3.Finally, backtracking starts with the highest-scored cell and goes back to the cell with a score of zero. In addition, the traceback method is exactly the same as the Needleman-Wunsch algorithm.

There are some examples in the Squence folder.

You can run the algorithm with the following command line:
> python Needleman-Wunsch.py
The default input file is:
'Sequence/Seq1.fasta'	and	'Sequence/Seq2.fasta'

If you want to change the default intput file,You can use the command line:
> python Needleman-Wunsch.py --file1=filename 
For example, you can change the default file1 to 'Squence/Seq3.fasta'
> python Needleman-Wunsch.py --file1=~/Sequence/Seq3.fasta

similarly,you can change the defaule file2:
> python Needleman-Wumsch.py --file2=filename

However, it should be noted that the file format you import must be the same as the instance file, that is, the standard FASTA format file.

In this algorithm, the default scoring system, match score is 1, and mismatch the score is -1, if you want to change the score arrangement, you can use the following command line:
> python Needleman-Wumsch.py --match = num1 --mismatch = num2
For example, you can change the default score system, change the matching score to 2, and mismatch the corresponding score to -2.
>python Needleman-Wumsch.py --match = 2 --mismatch = -2

If you want to ask for help, you can use the following command line, although it does not make much difference:
> python Needleman-Wunsch.py -h




At present, the algorithm still has some deficiencies:

Can not solve the left and above the same score obtained by the backtracking branch path problem

If you have good ways to improve, look forward to your email
# Smith-Waterman
