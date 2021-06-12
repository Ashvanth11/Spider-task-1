# Algos task-1
## Questions:
**A)** 

Sri Harsha is a very curious fellow. He started to wonder about binary numbers and how you can represent them as strings. But, due to his exceptional nature, this was not enough for him. He wondered if a binary string could be decomposed into the average of two different binary strings of equal length as the original string.

If there are multiple answers, you need to print the strings that make the differnce of 2 numbers minimum.

**Example:**  1101 (13) can be expressed as the average of 1011 (11) and 1111 (15), or 1100 (12) and 1110 (14) , So the answer will be 1110 and 1100.

**Note:**  length of both strings should be same and don't use leading zeros.

**Input Format**

The first line is the length of the string.  
The second line is the string.

**Constraints**

Length of the string<=100000  
The string is composed of zeroes or ones.

**Output Format**

If it is not possible to print two strings pertaining to the conditions prescribed the print –1 on one line.  
Otherwise, output 2 space-separated strings with the first string being the lesser string  

The strings should obey the conditions prescribed above.
<br />
<hr />
**B)**

Degree of symmetry is defined as the numbers of times you can divide (if can divide) a string such that both the remaining half are equal to each other.

**Examples:**  
_A_: The degree of symmetry is 0 as it cannot be divided.  
_ABAB_  : The degree of symmetry is 1. It can be divided only once into AB - AB which can’t be divided further into equal strings.  
_AAAA_: The degree of symmetry is 2. It can be divided into AA - AA, each AA can be further divided into A-A which cannot be divided any further.

**Input Format**

The First line contains an integer n denoting the length of string  
The Second line contains a String of length n.

**Constraints**

1 <= Length of the String <= 106.  
The Length of the String is always a Power of 2. (Note: 1 is a power of 2 (2^0))  
The String consists of lowercase Alphabets Only.

**Output Format**

Print an Integer denoting the Degree of Symmetry.
<br />
<hr />
***C)***

The  **SPIDER ALGO TEAM**  members have a strange connection with pizzas and the success of the workshop on that day. We consider a duration of workshop be n days each numbered from  **1**  to  **n**. You are given following information about each day:

1.  Whether they have a workshop on day i or not.
    
2.  whether they eat pizza on day i or not.
    

The team members become happy and hence the workshop turns out to be successful when the head of the team make eat pizza on the same day.The initial money which the spider Algo team has is  **Rs r**. For every successful workshop their money increases by  **Rs x**.For every unsuccessful workshop their total decrease by  **Rs y**. You have to determine the total money at the end of n days.

**Input Format**

The first line contains a positive integer n, r, x, y – the number of days under consideration, his initial amount, increase after each Successful workshop , and the decrease in their total after each unsuccessful workshop respectively .  
The second line contains the sequence of integers c 1 , c 2 , ..., c n separated by space, where:  
- c i equals 1 if workshop completed successfully on the i- th day, 0 otherwise.  
The third line contains the sequence of integers s 1 , s 2 , ..., s n separated by space,   
- s i equals 1 if the team eats pizza on the i- th day, 0 otherwise.

**Constraints**

1 ≤ n ≤ 1000000  
1 ≤ r ≤ 3000  
1 ≤ x, y ≤ 100  
0 ≤ c[i] ≤ 1  
0 ≤ s[i] ≤ 1  

**Output Format**

· Print a single line containing the string “promoted”(without quotes) if the money the team earns is greater than their initial amount. · Print a single line containing the string “demoted”(without quotes) if the money is lesser than their initial amount. · Print “no change” otherwise.
<br />
<hr />
***D)***

Priya likes to play with numbers. One day Priya decides to assign a task to her mentee Tanya. You have to help Tanya to complete this task. Task is as follows - Priya gives sanya an integer  _N_  which is always a odd number. Priya wants Tanya to make a pattern which consists of  _N_  rows and  _N_  columns .Priya being Priya asked her to make pattern which will consist of  ' '(space)  and  * (character)  only. For making Tanya understand the type of pattern she wants Priya gave her a sample input and output.Your task is to Help tanya print the pattern.

**Input Format**

The first line of input contains an integer 'T' representing the number of test cases.

Then each test case contains a single integer ‘N’ denoting the size of the pattern.

**Constraints**

1 <= T <= 5  
3 <= N <= 500  

Where ‘T’ is the number of test cases, ‘N’ is the size of the pattern. ‘N’ will be odd for all test cases.

**Output Format**

For each test case, print the pattern.
<br />
<br />

## Explanation:
<p align="justify">
**ALGOS TASK 1**

*TASK 1-A*
- take in the binary string and its length
- convert it into decimal
- find the numbers immediately before and after the given number.(the difference between them is minimum)
- convert them into binary
- print them

*TASK 1-B*
- take in a string of letters and its length
- create a variable(ans) with initial value as 0. increase it by 1 whenever we find a degree of symmetry
- find the mid index of the string 
- define a function(check()) compares the first half of the string to the second half of the string, letter by letter
- call the function
- if symmetrical, divide the mid index by half and call the check() function again
- repeat it using a while loop as long as the string can no longer be broken into symmetrical parts
- print the answer(ans)

*TASK 1-C*
- take in the values
- create a variable(rf) and set it to initial amount-r 
- create a nested if-else statement to increase rf by x in successful days and decrease it by y in unsuccessful days
- place it under a for loop with range to check it for all the days
- compare rf to r and print the final answer

*TASK 1-D*
- def functions r1() and r2() to print '*'(character) and ' '(space) respectively
- define function pattern()
- call r1() to print first line
- create two variables(k,l) and a while loop to print the remaining lines till the mid line which has just two '*'
- call the functions in the order: r1(),r2(),r1() since each line is made up of '*', space and then '*' again
- increase/decrease k,l accordingly
- create another while loop and two variables(u,v) to print the rest of the lines except the last line
- call r1() to print the last line
- take in the number of test cases
- take in the size of each test case and store it in a list(a[]) using for loop
- call pattern() for each test case using for loop
</p>
<br />
<br />
> Done by: Ashvanth (110120017)
