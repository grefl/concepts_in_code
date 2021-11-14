

# SPF -> Sender Policy Framework record
# Used to tell mail exchanges which hosts are authorized to send mail for a domain
# STATUS: Deprecated - Replaced by TXT Record

EXAMPLE_SPF_RECORD = 'v=spf1 a mx ip4:69.64.153.131 include:_spf.google.com ~all'
def warn_of_unused_prt(string):
    if string.index('ptr'):
        print('WARNING: type -> ptr should not be used')

mechanisms = '''
    all
    include
    a
    mx
    ip4
    ip6
    exists
'''

modifiers = '''
    redirect
    exp
'''
def get_spf_version(string):
    start = string.index('v=')
    if start == -1:
        return None
    end = string.index(' ', start)
    return string[start:end]
     
    return string[start:end]
print(get_spf_version(EXAMPLE_SPF_RECORD))
