
root = {'data': 'A', 'children': [{'data': 'B', 'children':
[{'data': 'D', 'children': []}]}, {'data': 'C', 'children':
[{'data': 'E', 'children': [{'data': 'G', 'children': []},
{'data': 'H', 'children': []}]}, {'data': 'F', 'children': []}]}]}


def preorderTraverse(node):
    print(node['data'], end = ' ' )
    if len(node['children']) > 0:
        #recursive case
        for n in (node['children']):
            preorderTraverse(n)
    #base case
    return 

def postorderTraverse(node):
    for n in (node['children']):
        #recursive case
        postorderTraverse(n)
    print(node['data'], end = ' ' )
    #base case
    return 


    

def inorderTraverse(node):
    if len(node['children']) >= 1:
        #recursive case
        inorderTraverse(node['children'][0])
    print(node['data'], end = ' ' )
    if len(node['children']) >= 2:
        #recursive case
        inorderTraverse(node['children'][1])
    # base case
    return 

def getDepth(node):
    if len(node['children']) == 0:
        # Base Case Return 0
        return 0
    else:
        #recursive case
        maxChildDepth = 0
        for n in node['children']:
            x = getDepth(n)
            if x> maxChildDepth:
                maxChildDepth = x
        return maxChildDepth +1



        

print('PRE:')
preorderTraverse(root)
print('Post:')
postorderTraverse(root)
print('In:')
inorderTraverse(root)
print('get Depth:')
print(getDepth(root))

