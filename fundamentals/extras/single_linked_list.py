class SLNode:
    def __init__(self, value):
        self.value=value
        self.next=None

class SList:
    def __init__(self):
        self.head=None
    
    def add_to_front(self, value):
        new_node=SLNode(value)
        current_head=self.head
        new_node.next=current_head
        self.head=new_node
        return self
    
    def add_to_back(self, value):
        if(self.head==None):
            self.add_to_front(value)
            return self
        new_node=SLNode(value)
        runner=self.head
        while(runner.next != None):
            runner=runner.next
        runner.next=new_node
        return self
    
    def remove_from_front(self):
        if(self.head!=None):
            if(self.head.next==None):
                value = self.head.value
                self.head=None
                return value
            value=self.head.value
            self.head=self.head.next
        return value
    
    def remove_from_back(self):
        if(self.head!=None):
            if(self.head.next==None):
                self.remove_from_front()
                return self
            runner=self.head
            next_node=runner.next
            while(next_node.next!=None):
                runner=next_node
                next_node=next_node.next
            runner.next=None
            return next_node.value
        return self

    def remove_value(self, value):
        if(self.head!=None):
            prev_node=self.head
            if(prev_node.value==value):
                return self.remove_from_front()
            runner=prev_node.next
            while(runner!=None):
                if(runner.value==value):
                    if(runner.next==None):
                        return self.remove_from_back()
                    prev_node.next=runner.next
                    return runner.value
                prev_node=runner
                runner=runner.next
        return self

    def insert_at(self, value, n):
        if(n<=0)or(self.head==None):
            self.add_to_front(value)
            return self
        new_node=SLNode(value)
        runner=self.head
        for idx in range(n):
            if(runner.next==None):
                runner.next=new_node
                return self
            prev_node=runner
            runner=runner.next
        # if(runner.next==None):
        #     self.add_to_back(value)
        #     return self
        prev_node.next=new_node
        new_node.next=runner
        return self

                # if(runner.value==value):
                #     if(runner==self.head):
                #         return self.remove_from_front()
                #     elif(runner.next==None):
                #         return self.remove_from_back()
                #     else:


    def print_values(self):
        runner=self.head
        while(runner != None):
            print(runner.value)
            runner=runner.next
        return self

my_list=SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
print("**************")
print(my_list.remove_from_front())
print("**************")
my_list.print_values()
print("**************")
print(my_list.remove_from_back())
print("**************")
my_list.print_values()

new_list=SList()
new_list.add_to_front("c").add_to_front("b").add_to_front("a").add_to_back("d").add_to_back("e").add_to_back("f").print_values()
print("**************")
print(new_list.remove_value("c"))
print("**************")
new_list.print_values()
print("**************")
print(new_list.remove_value("a"))
print("**************")
new_list.print_values()
print("**************")
print(new_list.remove_value("f"))
print("**************")
new_list.print_values()
print("**************")
new_list.insert_at("w", 0)
new_list.print_values()
print("**************")
new_list.insert_at("w", 2)
new_list.print_values()
print("**************")
new_list.insert_at("w", 4)
new_list.print_values()
print("**************")
new_list.insert_at("w", 10)
new_list.print_values()
print("**************")
new_list.insert_at("v", -1)
new_list.print_values()
print("**************")