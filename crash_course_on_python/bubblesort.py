arr=[8,3,0,4,1,7,6,2,5,9]




def bubblesort(theSeq):
	n=len(theSeq)
	#print(n)
	for i in range (n-1):
		#print('/////////')
		for j in range (n-1-i):
			#print(j)
			if theSeq[j]>theSeq[j+1]:
				tmp=theSeq[j]
				theSeq[j]=theSeq[j+1]
				theSeq[j+1]=tmp
	return theSeq			



print(bubblesort(arr))




import datetime


date1=datetime.date(2016,1,7)
print(date1,date1.year,date1.month)
