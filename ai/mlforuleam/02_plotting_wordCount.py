import matplotlib.pyplot as plt
import csv


x=[]
y=[]


# with open('count_vs_words','r') as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         print(row)


counter=0
with open('count_vs_words','r') as file:
    csvreader = csv.reader(file, delimiter=' ')
    for row in csvreader:
        #print(type(row))
        # print(row)
        # print(row[1])
        #print('Counter: ',counter)
        #counter=counter+1
        y.append(int(row[0]))
        x.append(str(row[1]))



#remove the first line
y=y[1:]
x=x[1:]
#plot
x_=range(len(y))
plt.figure(figsize=(10,10))
plt.plot(x,y,'*')
plt.show()






# stop = 5;

# for i in range(stop): # default values for start and step which is 1

#     print(i);
