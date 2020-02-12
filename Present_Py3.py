#Present Algo implementation in Python3

###Functions

def to_bin(a):
    return "{0:04b}".format(int(a,16))

def to_hex(a):
    return hex(int(a,2))[-1].upper()



def S_box(a):
    return to_bin(S[to_hex(a)])

S={
    "0":"C", "1":"5", "2":"6", "3":"B",
    "4":"9", "5":"0", "6":"A", "7":"D",
    "8":"3", "9":"E", "A":"F", "B":"8",
    "C":"4", "D":"7", "E":"1", "F":"2"
    }
P=[
    0,16,32,48,1,17,33,49,2,18,34,50,3,19,35,51,
    4,20,36,52,5,21,37,53,6,22,38,54,7,23,39,55,
    8,24,40,56,9,25,41,57,10,26,42,58,11,27,43,59,
    12,28,44,60,13,29,45,61,14,30,46,62,15,31,47,63
    ]



def gen_roundkeys(key,rounds):

    key_list=[]

    for i in range(1,rounds+1):
        #Step 1 : Store leftmost 64 bits as roundkey
        key_cp=str(key)
        key_list.append(key_cp[:64])

        #Step 2 : Shift the whole thing 61 bits to the left
        key=key[-19:]+key[:-19]

        #Step 3 : S box
        key=S_box(key[:4])+key[4:]

        #Step 4 : Xor with round counter
        key=key[:-20]+"{0:05b}".format(int(key[-20:-15],2)^i,2)+key[-15:]

    return key_list


def SP_Layer(state):

    #Check length of state to be 64

    upd=''
    
    #S Layer
    #pass every 4 bit into S boxes individually
    for i in range(16):
        upd+=S_box(state[4*i:4*(i+1)])

    #P Layer
    fl="3"*64

    for i in range(len(upd)):
        fl[P[i]]=upd[i]

    return fl


def encrypt(pt,key):
    #Encryption 31 round with 80Bits key and 64Bits block

    round_key_list=gen_roundkeys(key,32)

    stat=
    
    
        

    

        
    



        
        
        
