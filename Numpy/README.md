# Numpy : Basic to Advance Level

## Introduction

NumPy is a core Python library for numerical computing, built for handling large arrays and matrices efficiently.

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/2df7a655-1b8c-4563-b728-568314d65174" />


# Array Manipulation
Creating NumPy arrays is a fundamental aspect of working with numerical data in Python.NumPy provides various methods to create arrays efficiently, catering to different needs and scenarios. 

NumPy provides several built-in functions to generate arrays with specific properties.

- np.zeros(): Creates an array filled with zeros.
- np.ones(): Creates an array filled with ones.
- np.full(): Creates an array filled with a specified value.
- np.arange(): Creates an array with values that are evenly spaced within a given range.
- np.linspace(): Creates an array with values that are evenly spaced over a specified interval.

## Simple Program of above function:

  <img width="902" height="810" alt="image" src="https://github.com/user-attachments/assets/f8710adf-745d-482a-836e-859b31f22c64" />

# Create Python Numpy Arrays Using Random Number Generation
NumPy provides functions to create arrays filled with random numbers.

- np.random.rand(): Creates an array of specified shape and fills it with random values sampled from a uniform distribution over [0, 1).
- np.random.randn(): Creates an array of specified shape and fills it with random values sampled from a standard normal distribution.
- np.random.randint(): Creates an array of specified shape and fills it with random integers within a given range.

## Simple code examples :
<img width="953" height="441" alt="image" src="https://github.com/user-attachments/assets/e28639a3-1a64-4ed0-9df6-308f5f20ea6f" />
# Create Python Numpy Arrays Using Matrix Creation Routines
NumPy provides functions to create specific types of matrices.

np.eye(): Creates an identity matrix of specified size.
- np.diag(): Constructs a diagonal array.
- np.zeros_like(): Creates an array of zeros with the same shape and type as a given array.
- np.ones_like(): Creates an array of ones with the same shape and type as a given array.

## Simple code examples :
<img width="637" height="505" alt="image" src="https://github.com/user-attachments/assets/dd374bf9-a45b-4948-be42-408deaf209dd" />





# Numpy Array Indexing
Array indexing in NumPy refers to the method of accessing specific elements or subsets of data within an array.This feature allows us to retrieve, modify and manipulate data at specific positions or ranges helps in making it easier to work with large datasets.

## Accessing Elements in 1D Arrays
- A 1D NumPy array is a sequence of values with positions called indices which starts at 0.
- We access elements by using these indices in square brackets like arr[0] for the first element. Negative indices count from the end so arr[-1] gives the last element.

  ## Simple Code example :
  <img width="679" height="251" alt="image" src="https://github.com/user-attachments/assets/c06a707c-a8c8-4822-88c5-df83e937b427" />
# Accessing Elements in Multidimensional Arrays
### 2D Arrays
We can access elements by specifying both row and column indices like matrix[row, column].
  <img width="1376" height="179" alt="image" src="https://github.com/user-attachments/assets/1481c317-9650-458c-a979-dd4c34fce738" />
 
 ### 3D Arrays
 It can be visualized as a stack of 2D arrays, we need three indices-
- Depth: Specifies the 2D slice.
- Row: Specifies the row within the slice.
- Column: Specifies the column within the row.
  We can access elements by specifying row, column and depth indices like matrix[depth, row, column].
  
<img width="539" height="292" alt="image" src="https://github.com/user-attachments/assets/2f08aba5-8a2a-4e3d-87c2-78844e4ee181" />




## Slicing Arrays
It allows us to extract a range of elements using the format start:stop:step

### Slicing 1D Arrays
For a 1D array, slicing returns a subset of elements between the start and stop indices.
<img width="620" height="151" alt="image" src="https://github.com/user-attachments/assets/ba11eb50-2682-4e04-9452-ae816949e195" />

Here arr[0:4] slices the array starting at index 0 up to (but not including) index 4 so it returns the elements [0,1, 2, 3].
## Slicing Multidimensional Arrays
In this slicing can be applied to each dimension separately which allows us to extract submatrices or smaller blocks of data.
<img width="574" height="219" alt="image" src="https://github.com/user-attachments/assets/195eac8c-e78d-4051-b8c4-c7029d2fc78e" />


## Boolean Indexing
It allows us to filter elements from an array based on a condition and returns only those that meet it
<img width="624" height="160" alt="image" src="https://github.com/user-attachments/assets/6a207b0b-da8e-472b-80b1-846d2f03f6bd" />

We can also use logical operators like & (AND), | (OR) and ~ (NOT) to combine conditions.
<img width="614" height="175" alt="image" src="https://github.com/user-attachments/assets/bfb77510-e283-4df9-a04d-344435028329" />



## Ellipsis (...) in Indexing
The ellipsis (...) can be used to select all dimensions which are not explicitly mentioned.
<img width="589" height="231" alt="image" src="https://github.com/user-attachments/assets/3eecf4d0-c3a4-4583-8e9c-812d5c50c41e" />


## Using np.newaxis to Add New Dimensions
The np.newaxis keyword adds a new axis to the array which helps in converting a 1D array into a row or column vector.
<img width="556" height="282" alt="image" src="https://github.com/user-attachments/assets/ea523007-8729-4c45-80f5-5e4cf95b3cf4" />
## Modifying Array Elements
We can modify array elements directly by using indexing or slicing. This makes it easy to update specific elements or ranges of elements in an array.


<img width="533" height="197" alt="image" src="https://github.com/user-attachments/assets/fad1d5b3-6d7c-422b-a72b-6708d232a4df" />



 # Reshape NumPy Array - Python

 Reshaping in NumPy refers to modifying the dimensions of an existing array without changing its data. 
 <img width="526" height="157" alt="image" src="https://github.com/user-attachments/assets/8e661dd7-19a9-4ec2-bdc8-3d36a5b1f870" />


 
 a.reshape(2, 3) arranges the 6 elements into 2 rows and 3 columns, forming a 2-D matrix.


 <img width="592" height="232" alt="image" src="https://github.com/user-attachments/assets/c50b93f5-5fe8-49f8-9eac-e4314c13a2af" />

 
 a.reshape(2, 2, 2) transforms the array into 2 blocks, each containing a 2×2 matrix, forming a 3-D structure.


<img width="640" height="244" alt="image" src="https://github.com/user-attachments/assets/8e8e8f8e-7f4c-4bf3-bb6b-438ecc74d9a5" />

a.reshape(3, -1) tells NumPy to create 3 rows, and it computes the remaining dimension as 4 columns, since 12 ÷ 3 = 4.


# NumPy Array Broadcasting
Broadcasting in NumPy allows us to perform arithmetic operations on arrays of different shapes without reshaping them. It automatically adjusts the smaller array to match the larger array's shape by replicating its values along the necessary dimensions.

<img width="701" height="215" alt="image" src="https://github.com/user-attachments/assets/8fd9a182-910b-4e24-b5ec-f8699bf81d7e" />


In this example, the scalar value 10 is broadcasted to match the shape of the 2D array. As a result the scalar 10 is added to each element of the 2D array creating a new array where each element is increased by 10 which results in the output.

## Example 1: Broadcasting a Scalar to a 1D Array
 <img width="653" height="166" alt="image" src="https://github.com/user-attachments/assets/86912b6a-7686-4cf0-9ff8-b8dbb96ed875" />

 ## Example 2: Broadcasting a 1D Array to a 2D Array
 <img width="631" height="203" alt="image" src="https://github.com/user-attachments/assets/d6b30680-70e5-4cbe-a420-c2492752707d" />

 ## Example 3: Broadcasting in Conditional Operations
 <img width="688" height="193" alt="image" src="https://github.com/user-attachments/assets/8822f08f-811f-4daa-a284-1904d76603a6" />

 ## Example 4: Using Broadcasting for Matrix Multiplication
 <img width="480" height="220" alt="image" src="https://github.com/user-attachments/assets/494ac026-5028-4c27-973f-25069de132df" />















