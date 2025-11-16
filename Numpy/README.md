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




 







