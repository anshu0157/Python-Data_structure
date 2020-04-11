from stack import stack

def is_match(ob,cb):
    if ob == '(' and cb ==')':
        return True
    elif ob == '{' and cb =='}':
        return True
    elif ob == '[' and cb ==']':
        return True
    else:
        return False

def balancing_br(mystr):
    s=stack()
    is_balance=True
    index=0
    while index < len(mystr) and is_balance:
        o_br=mystr[index]
        if o_br in '({[':
            s.push(o_br)
        else:
            if s.is_empty:
                is_balance= False
            else:
                top=s.pop()
                if not is_match(top,o_br):
                    is_balance=False
        index+=1
    if s.is_empty and is_balance:
        return True
    else:
        return False
print(balancing_br('{{}}'))
