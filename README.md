# 371A1

## Contributors

    Name: Andrew Hunter-Owega
    Email: ahunterow@unbc.ca
    Student Number: 230 147 039

    Name: Daniel Strickland
    Email: dstrickla@unbc.ca
    Student Number: 230 146 357

    Name: Nicholas Hirt
    Email: nhirt@unbc.ca
    Student Number: 230 127 295
    
## Project Description

    CPSC 371 Artificial Intelligence Assignment #1
    
    The purpose of this assignment is to develop a better understanding of dynamic programming in practice.
    This is done through a investigation of the Knapsack Problem(KP) including the following subcategories:
      1.) Simple 0-1 Knapsack Problem,
      2.) General Knapsack Problem,
      3.) Knapsack Problem with constraints.
    The project will take input from a user specified file(.txt) or from the default file implemented within the project space.
    The user will select which version of the knapsack problem they would like to see the solution to.
    The project will scan through the file and appropriately parse text within the file to create item objects and extract further constraints that this iteration of the project will deal with.
    The project will utilize dynamic programming to realize the best solution to the current iteration of the knapsack problem.
    The project will print the solution to the Knapsack Problem to the GUI as well as to a file(.txt) either user specified or a default file.
    
## Project Description

  The project is composed of a series of functions, objects, and classes as described below:
  
  ex1.py:
  This file is the entry point for our project and includes the definitions of our gui.
  This means that it is responsible for actions such as button presses and file selections.
  However, it is not responsible for dynamic programming logic, file parsing, or object handling.
  
  knapsack_item.py:
  This file contains the objects that contain each item's information such as: item ID, item weight, and item price.
  It also implements standard getter methods for accessing the properties of each item.
  
  parse.py:
  This file is responsible for parsing information inside of input files.
  It implements methods to both scan through the input file line by line and to distinguish between the data provided.
  It will be able to create item objects based on relevant info and identify the capacity of the knapsack.
  
  knapsackProblems.py:
  Responsible for using logic within items to solve knapsack problems utilizing dynamic programming.
  Utilizes several different methods to solve knapsack problem constraints based upon user input.
