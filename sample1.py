m = 12;
def PrintList(mylist):
    print("PrintfList function");
    lenlist=len(mylist);
    print(lenlist);
    i =0;
   # while ()

def f1():
    m = "mai";
    s = '''Happy you 
    to you
    Happy birthday to 
    you. ''';
    print('Hello from f1: ', m); 
    s2=s.lower();
    print(s2);
    count=0;
    if ('you' in s2):
        count+=1;
    print (s);
    print('count = ' , count);
f1();
print ('Value of m: ', m);
list1 = ["apple", "banana", "mango","star","jackfruit"];
for i in list1:
    print(i);
for i in range(len(list1)):
    print(list1[i]);
PrintList(list1);
print('\nDictionary\n');
dic1 = {
    'name': 'maimai',
    'course': 'cpe',
    'year':'3'
    };
print(dic1);
course = dic1.get("course");
print (course);
if course=='cpe':
    print("Good CPE");
elif course =='bsit':
    print("OK IT");
elif course == 'bsce':
    print("OK CE");
else:
    print("OK");
    
