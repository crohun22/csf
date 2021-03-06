# Name: Hunter Crook
# Evergreen Login: crohun22
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name

if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
Total_count = 0


# Number of nucleotides seen so far.
gc_count = 0
at_count = 0
a_count = 0
t_count = 0
c_count = 0
g_count = 0
ratio = 0.0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    Total_count = Total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
    
    # next, if the bp is a A or a T,
    if bp == 'A' or bp == 'T':
        # increment the count of at
        at_count = at_count + 1
    
    # next, if the bp is an a A nucleotide,
    if bp == 'A':
        # increment the count of a
        a_count = a_count + 1
    # next, if the bp is an a T nucleotide,
    elif bp == 'T':
        # increment the count of T
        t_count = t_count + 1
    # next, if the bp is an a C nucleotide,
    elif bp == 'C':
        # increment the count of C
        c_count = c_count + 1
    # next, if the bp is an a G nucleotide,
    elif bp == 'G':
        # increment the count of G
        g_count = g_count + 1


# divide the gc_count by the total_count
gc_content = float(gc_count) / Total_count

# divide the at_count by the atTotal_count
at_content = float(at_count) / Total_count

# divide the a_count by the aTotal_count
a_content = float(a_count) / Total_count

# divide the t_count by the tTotal_count
t_content = float(t_count) / Total_count

# divide the c_count by the cTotal_count
c_content = float(c_count) / Total_count

# divide the g_count by the gTotal_count
g_content = float(g_count) / Total_count

# Divide the AT count by the GC count to get the ratio
ratio = at_count/gc_count


# Print the answer
print 'GC-content:', gc_content
if (gc_content >= 0.6):
    print 'This organism is a high GC content.'
elif gc_content <= 0.4:
    print 'This organism is a low GC content.'
else:
    print 'This organism is a moderate GC content.'
print 'AT-content:', at_content
print 'The AT/GC ratio is: ', ratio

print 'A count:', a_count
print 'T count:', t_count
print 'G count:', g_count
print 'C count:', c_count
print 'The sum of the a,c, t, g is: ', Total_count
print 'The total length is: ', len(seq)

#no collaboration