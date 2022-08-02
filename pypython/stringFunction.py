word="CESAR SINCHIGUANO"



word.lower()
print(word.lower())
print(word)


s="    Extras  \n"
print(s)
print(s.strip())

a="$$$$$$$$Cesar Sinchiguano$$$$$$$$$$"
print(a.strip('$'))


p="cesar augusto sinchiguano chiriboga"


print(p.split())


k="hello"
print(k[4:7])
print(k[-4:-1])

print("he" in k)
print(k.find('el'))


statement="We love {} {}"
t=statement.format('data','analysis')
print(t)