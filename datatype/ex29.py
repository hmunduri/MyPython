#Python program to set the indentation of the first line 
import sys 
import textwrap
sample_text = '''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    '''
#text1 = textwrap.dedent(sample_text).strip()
print()
print(textwrap.fill(sample_text,
                   initial_indent='',
                   subsequent_indent=' ' * 4, 
		   width = 80, 
		   ))
print()
