#2 Practice2: multiplication_table

i = 1 #Outer loop variable, controls rows(1-9)
while i <= 9:
    j = 1 #Inner loop variable, controls columns in each row
    while j <= i: #Each row only prints up to the current row number
        print(f"{j}*{i}={j*i}\t", end='')
        j += 1 #Increment column number
    i += 1 #Increment row counter
    print() #New line after each row