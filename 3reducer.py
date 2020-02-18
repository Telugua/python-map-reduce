s = open("02.txt","r")
r = open("03.txt", "w")

count = 0
thisKey = ""
thisValue = 0
for line in s:
  data = line.strip().split('\t')
  paymentType, cost = data

 

  if paymentType != thisKey:
    # output the last key value pair result

    if thisKey != "":
      r.write(thisKey + '\t' + str(count) + '\n')

    count = 0
    thisKey = paymentType 
    # start over when changing keys

  if paymentType == thisKey:
       count += 1
  

  # apply the aggregation function  
r.write(thisKey + '\t' + str(count))


# output the final entry when done
#r.write(thisKey + '\t' + str(thisValue)+'\n')
#print(thisKey+ str(count))
s.close()
r.close()