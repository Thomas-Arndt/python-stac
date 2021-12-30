class DNode:
    def __init__(self, value):
        self.value=value
        self.prev=None
        self.next=None
    

class DList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add_to_end(self, value):
        new_node=DNode(value)
        if(self.tail==None):
            self.head=new_node
            self.tail=new_node
            return self
        new_node.prev=self.tail
        self.tail.next=new_node
        self.tail=new_node
        return self
    
    def remove_value(self, value):
        runner=self.head
        while(runner!=None):
            if(runner.value==value):
                runner.prev.next=runner.next
                runner.next.prev=runner.prev
                return value
            runner=runner.next
        return self

    def insert_at(self, value, n):
        new_node=DNode(value)
        if(n<=0) or (self.head==None):
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
            return self
        runner=self.head
        for idx in range(n):
            if(runner.next==None):
                new_node.prev=runner
                runner.next=new_node
                return self
            runner=runner.next
        new_node.next=runner
        new_node.prev=runner.prev
        runner.prev.next=new_node
        runner.prev=new_node
        return self
    
    def insert_before(self, value, match):
        new_node=DNode(value)
        runner=self.head
        while(runner != None):
            if (runner.value==match):
                runner.prev.next=new_node
                new_node.prev=runner.prev
                new_node.next=runner
                runner.prev=new_node
                return "Success!"
            runner=runner.next
        self.add_to_end(value)
        return "Match not found. Node added to end of list."
    
    def insert_after(self, value, match):
        new_node=DNode(value)
        runner=self.head
        while(runner != None):
            if (runner.value==match):
                runner.next.prev=new_node
                new_node.next=runner.next
                new_node.prev=runner
                runner.next=new_node
                return "Success!"
            runner=runner.next
        self.add_to_end(value)
        return "Match not found. Node added to end of list."

    def find_middle_value(self):
        head_runner=self.head
        tail_runner=self.tail
        while(head_runner!=tail_runner) and (head_runner.next!=tail_runner):
            head_runner=head_runner.next
            tail_runner=tail_runner.prev
        return head_runner.value

    def remove_duplicates(self):
        values_present={}
        head_runner=self.head
        tail_runner=self.tail
        while(head_runner!=tail_runner) and (head_runner.prev!=tail_runner):
            if head_runner.value not in values_present:
                values_present[head_runner.value]=True
            else:
                head_runner.prev.next=head_runner.next
                head_runner.next.prev=head_runner.prev
            if tail_runner.value not in values_present:
                values_present[tail_runner.value]=True
            else:
                tail_runner.next.prev = tail_runner.prev
                tail_runner.prev.next = tail_runner.next
            head_runner=head_runner.next
            tail_runner=tail_runner.prev
        return self
    
    # def reverse_list(self):
        
    #     return self

    
    def print_values(self):
        runner=self.head
        while(runner!=None):
            print(runner.value)
            runner=runner.next
        return self
    

new_list=DList()
new_list.add_to_end("a").add_to_end("b").add_to_end("c").add_to_end("d").add_to_end("e").add_to_end("f").print_values()
print("**************")
print(new_list.remove_value("c"))
print("**************")
new_list.print_values()
print("**************")
print(new_list.remove_value("e"))
print("**************")
new_list.print_values()
print("**************")
new_list.insert_at("w", 0)
new_list.print_values()
print("**************")
new_list.insert_at("x", 2)
new_list.print_values()
print("**************")
new_list.insert_at("y", 4)
new_list.print_values()
print("**************")
new_list.insert_at("z", 10)
new_list.print_values()
print("**************")
print(new_list.insert_before("1", "y"))
print("**************")
new_list.print_values()
print("**************")
print(new_list.insert_before("2", "g"))
print("**************")
new_list.print_values()
print("**************")
print(new_list.insert_after("5", "y"))
print("**************")
new_list.print_values()
print("**************")
print(new_list.insert_after("6", "u"))
print("**************")
print(new_list.insert_after("5", "u"))
print("**************")
print(new_list.insert_after("6", "u"))
print("**************")
print(new_list.insert_after("6", "u"))
print("**************")
new_list.print_values()
print("**************")
print(new_list.find_middle_value())
print("**************")
new_list.remove_duplicates()
new_list.print_values()
print("**************")
# new_list.reverse_list()
# new_list.print_values()
# print("**************")
