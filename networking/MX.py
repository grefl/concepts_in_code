
def create_mx_record(domain, priority):
    return { 'domain': domain, 'priority': priority }




class MX:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)


    def get_record(self, previous_record, index=0):
        if index >= len(self.records):
            return None, -1
        return self.records[index], index + 1 


p0 = create_mx_record('aspmx.l.google.com', 1)
p1 = create_mx_record('alt1.aspmx.l.google.com', 5)
p2 = create_mx_record('alt2.aspmx.l.google.com', 5)
p3 = create_mx_record('aspmx2.googlemail.com', 10)
p4 = create_mx_record('aspmx3.googlemail.com', 10)

mx = MX()
mx.add_record(p0)
mx.add_record(p1)
mx.add_record(p2)
mx.add_record(p3)
mx.add_record(p4)

domain, index = mx.get_record(None)
while domain:
    print(domain)
    domain, index = mx.get_record(domain, index)

