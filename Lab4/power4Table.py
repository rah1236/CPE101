# CPE 101 Lab 4
# Name:
# Section:

def main():
   table_size = get_table_size()
   while table_size != 0:
      first = get_first()
      show_table(table_size, first)
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
   return first;

# Display the table of power4
def show_table(size, first):
   print ("A power4 table of size %d will appear here starting with %d." % (size, first))
   print ("Number  Power4")
   
   # Insert Loop Here
   

if __name__ == "__main__":
   main()
