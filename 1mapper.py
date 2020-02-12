inp = open("purchases.txt", "r")
out = open("01.txt", "w")

for line in inp:
    datalist = line.strip().split("    ")
    date, time,store, item, cost, paymentType = datalist
    out.write(paymentType + "\t" + cost + "\n")

inp.close()
out.close()