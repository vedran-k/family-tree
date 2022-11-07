# family-tree
The input file for the python application has the following structure <child name> <parent name>
Example file:
Adam John
Marc Steven
Steven Adam
Robert Steven
Frank John
Leo Lukas
This python program which the input file as a cli argument and writes the resulting family tree into stdout:
John
  Adam
    Steven
      Marc
      Robert
  Frank
Lukas
  Leo
