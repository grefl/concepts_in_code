
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, node = None):
        self.head = node
        self.tail = self.head 
    def insert(self, node):
        if not self.head:
            self.head = node
            self.tail = self.head 
        else:
            self.tail.next = node 
            self.tail = node
    def remove(self):
        if self.head == self.tail:
            val = self.tail.val
            self.head = None
            self.tail = None
            return val
        else:
            val = self.head.val
            self.head = self.head.next
            return val

    def top(self):
        return self.head.val
    def end(self):
        return self.tail.val
    
    def print_all(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

class Records:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.cnames = LinkedList() 
        self.cnames.insert(Node({'A': self.name, 'ip': self.ip}))

    def set_A_name(self, name):
        self.name = name
    def set_A_ip(self, ip):
        self.ip = ip 
    def add_CNAME(self, name):
        self.cnames.insert(Node({'CNAME': name, 'alias': self.cnames.end()}))

    def print_all(self):
        self.cnames.print_all()
        

r = Records('github.map.fastly.net.', '185.31.17.133')
r.add_CNAME('aetrion.github.io.')
r.add_CNAME('blog.dnsimple.com.')

r.print_all()
