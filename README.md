## Family tree
The input file for the python application has the following structure: child_name parent_name

Example file:
~~~txt
Adam John
Marc Steven
Steven Adam
Robert Steven
Frank John
Leo Lukas
~~~

This python program takes the input file as a cli argument and writes the resulting family tree into stdout:
~~~txt
John
  Adam  
    Steven    
      Marc      
      Robert      
  Frank  
Lukas
  Leo
~~~
