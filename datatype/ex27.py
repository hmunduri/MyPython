#Python program to display formatted text(width=50) as output
import sys
import textwrap
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
test_without_Indentation = textwrap.dedent(sample_text)
print()
print(text_without_Indentation)
print()
