def contains_item(list_to_be_tested:list[str], value:str) -> bool:
    for element in list_to_be_tested:
        if element == value:
            return True
    return False

def add_item(l, valute_to_be_added):
    if not contains_item(list_to_be_tested=l, value=valute_to_be_added):
        l.append(valute_to_be_added)
    return l    

def remove_item(l:list[str], value_to_be_removed:str) -> list[str]:
    if contains_item(list_to_be_tested=l, value=value_to_be_removed):
        l.remove(value_to_be_removed)

    return l
# koment   
def replace_items(l:list[str], first_value:str, second_value:str) -> bool:
    to_return = False
    for index in range(0, len(l)):
        if l[index] == first_value:
            l[index] = second_value
            to_return = True

    return to_return
# druhý koment
def find_item(l:list[str], value:str) -> list[str]:
    for index in range(0, len(l)):
        if l[index] == value: # index = 1
            l[index] = str(index) #l[0] = 0

    return l
        

def revert_items(l:list[str]) -> list[str]:
    to_return = []
    # 0 -> len(l) - 1
    for index in range(len(l)-1, -1, -1):
        to_return.append(l[index])

    return to_return

def revert_items_in_place(l:list[str]) -> list[str]:
    
    i:int = 0
    j:int = len(l) - 1

    while( i < j):
        temp = l[i]
        l[i] = l[j]
        l[j] = temp

        i += 1
        j -= 1
    return l

def find_extreme(l:list[int], s:str) -> int:
    to_return = l[0]
    if s == "biggest":
        for x in l:
            if x > to_return:
                to_return = x

        #najdeme největší
    elif s == "smallest":
        for x in l:
            if x < to_return:
                to_return = x
    else:
        print("Wrong argument")
        return -1

    return to_return


def sort_my_list(l:list[int], flag:str) -> list[int]:
    to_return = []
    while len(l) > 0:
        #řafím vzestupně
        # nejprve potřebuju najít nejmenší číslo
            if flag == "asc":
                extrem = find_extreme(l=l, s="smallest")
            else:
                extrem = find_extreme(l=l, s="biggest")
            to_return.append(extrem)
            l.remove(extrem)
   
    return to_return


class Person:
    name:str
    age:int
    weight:str

    def __init__(self,name:str, age:int, weight:str) -> None:
        self.age = age
        self.name = name
        self.weight = weight

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __repr__(self) -> str:
        print("volam repr")
        return str(self.weight)

    def __add__(self, other) -> str:
        return self.name + other.name


class Zasobnik:
    index:int
    data:list[int]

    def __init__(self) -> None:
        self.data = [] #[42]
        self.index = -1 #0

    def push(self, to_be_pushed:int) -> None:
        self.index += 1
        self.data.append(to_be_pushed)
      

    def pop(self) -> int:
        to_return = self.data[self.index] #42
        del self.data[self.index] #[]
        self.index -= 1 #index = -1
        return to_return

    def peek(self) -> int:
        return self.data[self.index]

    def is_empty(self) -> bool:
        return self.index == -1

    def size(self) -> int:
        return self.index + 1




class Queue:
    index:int
    data:list[int]
    front:int

    def __init__(self) -> None:
        self.index = 0
        self.data = []
        self.front = 0

    def enqueue(self, to_be_added:int) -> None:
        self.data.append(to_be_added)
        self.index +=1
        

    def dequeue1(self) -> int:
        to_return = self.data[self.front]
        self.front += 1
        return to_return

    def dequque2(self) -> int: #self.data = [42, 22, 7]
        to_return = self.data[0] #to_return = 42
        new_data = [] # self.data = [42, 22, 7], new_data = []
        for x in range(1, len(self.data)): # x = 1, x = 2 x element <1, 3)
            new_data.append(self.data[x]) #new_data = [22, 7]
        self.data = new_data #self.data = [22, 7]

        return to_return



class Node:

    def __init__(self, value:int) -> None:
        self.value = value
        self.next_node = None


class LinkedList:
    head:Node
    count:int

    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def push_end(self, to_be_pushed:int) -> None:
        self.count += 1
        if self.head == None:
            node = Node(to_be_pushed)
            self.head = node
        else:
            node = Node(to_be_pushed)
            traversal = self.head
            while traversal.next_node != None:
                traversal = traversal.next_node
            traversal.next_node = node

    def push_beginning(self, to_be_pushed:int) -> None:
        count += 1
        if self.head == None:
            node = Node(to_be_pushed)
            self.head = node
            
        else:
            print("spustila se druha podminka")
            node = Node(to_be_pushed)
            print("self head pred pridanim " + str(self.head))
            prev_head = self.head
            print("prev head, mel by byt to same jako self head" + str(prev_head))
            self.head = node
            print("novy self head" + str(self.head))
            print("prev head by mel zustat nezmeneny" + str(prev_head))
            self.head.next_node = prev_head
            #v linked listu je alespon jeden element

    def is_empty(self) -> bool:
        return self.head == None

    def size(self) -> int:
        return self.count

    def del_first(self) -> Node:
        if self.is_empty():
            return None
        else:
            to_return = self.head # do proměné to_return uložím odkaz na první node
            self.head = to_return.next_node #self.head bude ukazovat na prvek na který ukazoval self.head.next_node
            to_return.next_node = None #mazu referenci, kterou měl prvni node na druhý
            self.count -= 1
    

            return to_return

    def del_last(self) -> Node:
        if self.is_empty():
            return None
        elif self.count == 1:
            to_return = self.head
            self.head = None
            self.count -= 1
            return to_return
        
        else: 
            traversal = self.head
            pre_traversal = None
            while traversal.next_node != None:
                pre_traversal = traversal
                traversal = traversal.next_node
            pre_traversal.next_node = None
            self.count -=1
            return traversal

    def reverse(self) -> None:
        pre_traversal = None
        traversal = self.head
        post_traversal = None
        if self.is_empty():
            return None
        if self.size() == 1:
            return None
        
        while traversal != None:
            post_traversal = traversal.next_node
            traversal.next_node = pre_traversal
            pre_traversal = traversal
            traversal = post_traversal
            #algoritmus

        self.head = pre_traversal

        return None

    def print_linked_list(self) -> None:
        traversal = self.head
        if traversal == None:
            print("Empty linked list")
            return

        while traversal != None:
            print(traversal.value)
            traversal = traversal.next_node
            
class NodeD:
    def __init__(self, value:int) -> None:
        self.value = value
        self.next_node = None
        self.prev_node = None



class DoublyLinkedList:
    head:NodeD
    tail:NodeD
    count:int

    def __init__(self) -> None:
        self.head = None
        self.count = 0
        self.tail = None

    def push_beginning(self, to_be_pushed:int) -> None:
        n = NodeD(to_be_pushed)
        if self.count == 0:
            self.head = n
            self.tail = n
        else:
            x = self.head
            self.head = n
            n.next_node = x
            x.prev_node = n
        self.count += 1
        

    def push_end(self, to_be_pushed:int) -> None:
        n = NodeD(to_be_pushed)
        if self.count == 0:
            self.head = n
            self.tail = n
        else:
            x = self.tail
            self.tail = n
            n.prev_node = x
            x.next_node = n
        self.count += 1

    def is_empty(self) -> bool:
        return self.count == 0

    def del_end(self) -> NodeD:
        if self.is_empty():
            return None
        elif self.count == 1:
            to_return = self.tail
            self.head = None
            self.tail = None
            self.count -= 1
            return to_return
        else:
            to_return = self.tail
            next_to_last = to_return.prev_node
            next_to_last.next_node = None
            self.tail.prev_node = None
            self.count -= 1
            self.tail = next_to_last
            return to_return

    def print_doubly_linked_list(self) -> None:
        traversal = self.head
        if traversal == None:
            print("Empty linked list")
            return

        while traversal != None:
            print(traversal.value)
            traversal = traversal.next_node





class Adresa:
    ulice:str
    mesto:str
    psc:str

    def __init__(self, ulice:str, mesto:str, psc:str) -> None:
        self.ulice = ulice
        self.mesto = mesto
        self.psc = psc

class Email:
    adresa:str

    def __init__(self, adresa:str) -> None:
        self.adresa = adresa


class Osoba:
    jmeno:str
    vek:int
    adresa:Adresa
    email:Email

    def __init__(self, vek:int, jmeno:str, adresa:Adresa, email:Email) -> None:
        self.vek = vek
        self.jmeno = jmeno
        self.adresa = adresa
        self.email = email


class Student(Osoba):
    skola:str

    def __init__(self, vek: int, jmeno: str, adresa: Adresa, email: Email, skola:str) -> None:
        super().__init__(vek, jmeno, adresa, email)
        self.skola = skola


class StudentKompo:
    skola:str
    osoba:Osoba

    def __init__(self, skola:str, osoba:Osoba) -> None:
        self.skola = skola
        self.osoba = osoba



adresa = Adresa(ulice="Petýrkova", mesto="Praha", psc="14800")

osoba = Osoba(jmeno="Filip", vek=28, adresa=adresa)

print(osoba.adresa.mesto)

