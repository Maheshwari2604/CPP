class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None

    def push(self , new_node):
        new_node = node(new_node)
        new_node.next = self.head
        self.head = new_node
def binaryfunc(arr, l, r, x):
    while l<=r:
        
        #finding the mid values
        mid = int(l+(r-l) / 2)

        #print(mid)
        #print(type(mid))
        
        #checking condition if mid value is equal to search value or not
        if(arr[mid] == x):
            return mid

        #if not and value is greater than mid value ignore left part and increase its value 
        elif arr[mid] < x:
            l = mid+1

                count += 1
                #print(temp.data)
                print('error')

        # middle = count/2 + 1
        # print(count)
        # print(middle)
        # print(type(middle))


        

if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.push(33)
    llist.push(411)
    llist.push(522)
    llist.push(623)
    llist.push(35589)
    llist.push(642)
    llist.push(9)
    llist.push(512)
    llist.push(33)
    llist.push(334)
    llist.middle_element()   
