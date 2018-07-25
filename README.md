# String-alignment-DP

This program reads a pair of strings from stdin. Each string will be on a single line by itself.
Be sure to strip off whitespace at each end of the strings, including
newlines.

The program aligns the pair of strings using the Needleman-Wunsch
algorithm. When there are choices in the traceback step, choose diagonal,
then left, and finally up.  Note there is a special case in which you may get
to the leftmost column before top row in which you merely keep the remaining
chars from the top string matched with '-'; similarly for getting to top
row before left column.

Run the program as follows:
    ./p5  match_value  mismatch_penalty  gap_penalty  ## strs entered at keybd
    ./p5  match_value  mismatch_penalty  gap_penalty < filename
For example:
    ./p5  +5  -4  -8  < file_containing_a_pair_of_strs  


Prints the alignment to stdout with the first string in the input printed
first on the output.
