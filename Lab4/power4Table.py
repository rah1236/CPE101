# CPE 101 Lab 4
# Name:Raheel Rehmatullah
# Section:7


#Purpose: Read a string and see if it has the word "Accepted" in it
# none -> none
def read_str():
    inputString = ""
    while("accepted" not in inputString):
        inputString = input("Please enter a sentence with the word 'accepted' in it.")
    print("Cool, thank you!")

#Purpose: Computes the factorial of given integer
# int -> float
def factorial(number):
    newNumber = abs(int(number))
    product = newNumber
    for i in range(1, newNumber):
        product *= i
    return product

#purpose: Takes income and computes income tax following the given table
#int -> float
def income_tax(income):
    if (income >= 0 and income < 9950):
        return(0.10)
    elif(income >= 9951 and income < 40525):
        return(0.12)
    elif(income >= 40526 and income < 86375):
        return(0.22)
    elif(income >= 86376 and income < 164925):
        return(0.24)
    elif(income >= 164926 and income < 209425):
        return(0.32)
    else:
        return(0)

#purpose: This function must print the number that is divisible by 7 between the given interval and find the total and return the average of these numbers.
#int int -> float
def total_avg(num1, num2):
    divisibleBySeven = []
    sum = 0
    for i in range(num1, num2):
        if(i % 7 == 0):
            divisibleBySeven.append(i)
    if len(divisibleBySeven) > 0 :
        for i in divisibleBySeven:
            sum += i
        return (sum/(len(divisibleBySeven)))
    else:
        return(0)






def main():
   table_size = get_table_size()
   increment = get_increment()
   while table_size != 0:
      first = get_first()
      show_table(table_size, first, increment)
      table_size = get_table_size()

# Obtain a valid table size from the user
def get_table_size():
   size = int(input("Enter number of rows in table (0 to end): "))

   while (size) < 0:
      print ("Size must be non-negative.")
      size = int(input("Enter number of rows in table (0 to end): "))

   return size;

# Obtain the first table entry from the user
def get_first():
   first = int(input("Enter the value of the first number in the table: "))

   while (first) < 0:
      print ("First number must be non-negative.")
      first = int(input("Enter the value of the first number in the table: "))

   return first;

# Obtain the iterative table entry from the user
def get_increment():
   increment = int(input("Enter the increment between rows: "))

   while (increment) < 0:
      print ("Increment must be non-negative.")
      increment = int(input("Enter the increment between rows: "))

   return increment;


# Display the table of power4
def show_table(size, first, increment):
   print ("A power4 table of size %d will appear here starting with %d." % (size, first))
   print ("Number  Power4")
   sum = 0
   for i in range(first, size * increment + first, increment):
       text = ("{:<6} {:>6}").format(i, i**4)
       print(text)
       sum += (i**4)

   print("The sum of power4 is: " + str(sum))





if __name__ == "__main__":
   main()


#show_table(4,2, 1)
