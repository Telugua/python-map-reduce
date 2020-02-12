s = open("02.txt","r")
r = open("finalResult.txt", "w")

cnt = 0
thiskey = ""
thisvalue = 0

for line in s:

  data = line.strip().split('\t')
  paymentType, amount = data

  if thiskey == "":
    if paymentType:
      thiskey = paymentType

  # apply the aggregation function
  
  if paymentType == thiskey:
   
    cnt = cnt + 1
  else:
    r.write( thiskey + '\t' + str(cnt)+'\n')
    # start over when changing keys
    thiskey = paymentType
    
    cnt = 1

  # output final entry

r.write( thiskey + '\t' + str(cnt)+'\n')

s.close()
r.close()