# All portfolio assignments

# Assignment 2.1: OO in Python

class MyDeQue(MyQueue):
    def __init__(self, a=[]):
        MyQueue.__init__(self,a)
        pass
    
    def __str__(self):
        return super.__str__(self)
    
    def appendright(self, x):
        self.enqueue(x)
    
    def appendleft(self, x):
        self.insert(0,x)

    def popright(self):
        return self.pop(len(self)-1)
    
    def popleft(self):
        return self.dequeue()
    
    def reverse(self):
        super().reverse()
    
    def rotateright(self,n):
        i = 0
        while(i < n):
            self.appendleft(self.popright())
            i += 1
        
    def rotateleft(self,n):
        i = 0
        while(i < n):
            self.appendright(self.popleft())
            i += 1
        
d = MyDeQue()
print(d)
d.appendright(2)
print(d)
d.appendright(1)
print(d)
d.appendleft(4)
print(d)
d.reverse()
print(d)
d.rotateright(1)
print(d)
d.rotateleft(1)
print(d)
a = d.popright()
print(d)
print("Return value: ", a)
a = d.popleft()
print(d)
print("Return value: ", a)

#Assignment 2.2: eval en veiligheid 
class SimpleSecureEvaluator(object):
    # empty dictionary
    
    def __init__(self):
        self.d = {}
        pass
    
    def eval(self, expressie):
        expressionIndicator = expressie.find('=')
        if(expressie == 'mydir'):
            print(self.d)
        
        elif(expressionIndicator != -1):
            leftValue = expressie[0:expressionIndicator];
            
            rightValue = expressie[expressionIndicator+1:len(expressie)]
            #if voor niet een impressie
            if(rightValue.find('+')!= -1 or rightValue.find('-')!= -1 or rightValue.find('/')!= -1 or rightValue.find('*')!= -1):
                #expressie
                for i in self.d.keys():
                    index = rightValue.find(i)
                    if(index != -1):
                        #found a value
                        value = self.d.get(i)
                        rightValue = rightValue.replace(rightValue[index], str(self.d[i]))
                result = eval(str(rightValue))
                print("Result:", result)
                self.d[leftValue] = result
            else:
                self.d[leftValue] = rightValue
        else:
            for i in self.d.keys():
                    index = expressie.find(i)
                    if(index != -1):
                        #found a value
                        value = self.d.get(i)
                        expressie = expressie.replace(expressie[index], str(self.d[i]))
            print("Result:" , eval(expressie))
            
        pass

d = SimpleSecureEvaluator()
d.eval("i = 1")
d.eval("mydir")
d.eval("j = i + 1")
d.eval("mydir")
d.eval("j + 1")
d.eval("a = j + i + 2")
d.eval("mydir")

#opdracht 2.3.1: introspectie van functies 

import function_demo_3_6
import inspect

listElements = dir(function_demo_3_6)
print(listElements)
print()
for e in sorted(vars(function_demo_3_6).items()):
    if e[0] != '__builtins__':
        print(e)
        if(type(e[1]).__name__ == 'function'):
            print()
            print("Documentation: \n", type(e[1]).__doc__)
            print()
            print("Signature: ", inspect.signature(e[1]))
            print()

#Assignment 2.3.2 Introspectie van klassen
import class_demo_3_6

for e in sorted(vars(class_demo_3_6).items()):
        if(type(e[1]).__name__ == 'type'):
            print("Found class: ", e[0])

#Assignment 3.1.1: To function or not to function
def wave(string):
    #niet puur want: gebruikt loop
    output = ""
    for index, letter in enumerate(string):
        if index % 2 == 0:
            output += letter.upper()
        else:
            output += letter.lower()
    return output

def wait_for_password():
    #niet puur want: gebruikt loop en is dus in een andere state binnen de functie
    password = input("Say the magic word! ")
    while password != "secret":
        password = input("Say the magic word! ")
    
def set_width(new_width):
    #niet puur want: veranderd globale variable
    global width 
    width = new_width
    
def make_sense(temp_in_fahrenheit):
    #puur
    return ((temp_in_fahrenheit+459.67) * 5/9)

def latin(word):
    #puur
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return word + "ay"
    else:
        cons_cluster = "".join(takewhile(lambda x: x not in vowels, word))
        return(word[len(cons_cluster):] + cons_cluster + "ay")
    
def latinise(string):
    #puur
    return re.sub(r'[a-zA-Z]+', lambda m: latin(m.group(0)), string)
    
def say_it_in_latin(string):
    #niet puur want: I/O gebruik
    print(latinise(string))


#Assignment 3.3.2 Functies filteren 
my_functions = [lambda x: x + 1, lambda x: x * 2, lambda x: x - 5] #TODO

def apply_everything(functions: List[Callable[[int], int]], integer: int) -> int:
    if(len(functions) == 0):
        return integer
    return apply_everything(functions[1:], functions[0](integer))

def filter_even_on_input(functions: List[Callable[[int], int]], input: int) \
                         -> List[Callable[[int], int]]:
    if(len(functions) == 0):
        return []
    elif(not(functions[0](input) % 2)):
        return [functions[0]] + filter_even_on_input(functions[1:], input)
    else:
        return [] + filter_even_on_input(functions[1:], input)

filtered_functions = filter_even_on_input(my_functions, 47)
print(apply_everything(my_functions, 47))
print(apply_everything(filtered_functions, 47)) # should only be evens