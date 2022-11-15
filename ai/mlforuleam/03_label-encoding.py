from sklearn import preprocessing 



labels=preprocessing.LabelEncoder()

input_classes=['suzuki','ford','suzuki','kia','ford','bmw',
                'suzuki','ford','suzuki','toyota','ford','bmw']

labels.fit(input_classes)


for i, item in enumerate(labels.classes_):
    print(i,'->',item)




#MAPPING BETWEEN WORDS AND NUMBERS


y_testing=['suzuki','kia','ford',]   
lookForLabels=labels.transform(y_testing)

print("y_testing: ", lookForLabels)


lookForBrands=labels.inverse_transform(lookForLabels)
print(lookForBrands)
