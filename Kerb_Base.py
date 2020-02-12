#Kerberos Base

from random import randint
import xxhash

#Key Gen using random number generator and xxhash - Non Crytographic hashing
#Main function to generate list of clients associated with each server - Maintain records of clients and keys(randint)
# __ pvt
#Chest list of following format [key_used_for_encryption,[data_to_be_encrypted]]

#Classes

class Client:
    def __init__(self):
        self.cl_id=randint(100001,10000001)
        self.__key=xxhash.xxh32(str(self.cl_id),seed=self.cl_id).hexdigest()

    def temp_print(self):
        print("ID :",self.cl_id)
        print("Key :",self.__key)

    def connect_to(self,server,service):
        self.__temp_key_1=0
        
        a=serv_dict[server].base_auth(self.cl_id)    #First step - Client ID transmitted to Server(AS) without encryption
        if a is not None:
            print(a)
            c1,c2=a[0],a[1]
            if self.__key!=c1[0]:
                print("Keys dont match")
                return 0
                
            else:
                self.__temp_key_1=c1[1]

                a=serv_dict[server].auth_2(service,c2,[self.__temp_key_1,self.cl_id])
                if a is not None:
                    print(a)
                    d1,d2=a[0],a[1]

                    if self.__temp_key_1!=d1[0]:
                        print("Keys dont match!")
                        return 0

                    else:
                        self.__temp_key_2=d1[1]

                        a=serv_dict[server].serc_connect(service,d2,[self.__temp_key_2,self.cl_id])

                        if a==0:
                            print("Connection Unsuccessful!")
                        else:
                            print("Connection Successful!")

                            choice1=input("Do you want to send data (Y/n)? ")
                            if choice1 not in "NOnoNo":

                                while 1:
                                    dat=input("Enter Data (0 to quit) :")
                                    if dat!="0":
                                        a=serv_dict[server].serc_connect(service,d2,[self.__temp_key_2,self.cl_id],dat)
                                        print(a)
                                        print()
                                    else:
                                        print("Connection Terminated")
                                        break
                                    
                                
                                
                                
                        
                        
                        
                                

class Server:
    #includes AS, TGS, List of Services
    #Use rand
    def __init__(self):
        self.__serv_id=randint(10001,1000001)
        self.__serv_key=xxhash.xxh32(str(self.__serv_id),seed=self.__serv_id).hexdigest()
        
        #self.AS=Service("AS")
        #self.TGS=Service("TGS")

        self.__service_list={}
        self.__client_key_list={}
        self.__service_key_list={}

        self.__temp_key=0
        


    def add_services(self):
        a=input("Enter Service Name :")
        while a in self.__service_list.keys():
            a=input("Name already exists! Enter Service Name :")
            
        b=int(input("Enter Passkey to generate Random Key :"))
        self.__service_list[a]=Service(a,b)
        self.__service_key_list[a]=xxhash.xxh32(str(a),seed=b).hexdigest()

    def add_client(self,cl_id):
        self.__client_key_list[cl_id]=xxhash.xxh32(str(cl_id),seed=cl_id).hexdigest()

    def temp_print(self):
        print("ID :",self.__serv_id)

        for i in self.__client_key_list:
            print("Client ID :",i)
            print("Client Key :",self.__client_key_list[i])
            print()

        for i in self.__service_key_list:
            print("Service Name :",i)
            print("Service Key :",self.__service_key_list[i])
            print()

        print("Printing Service side Info")
        print()
        for i in self.__service_list:
            self.__service_list[i].temp_print()

    def base_auth(self,cl_id):
        print("First level Authentication ")
        if cl_id in self.__client_key_list:
            self.new_key_1=randint(101,1000001)
            while self.new_key_1 in self.__client_key_list.values():
                self.new_key_1=randint(101,1000001)
            self.new_key=xxhash.xxh32(str(cl_id),seed=self.new_key_1).hexdigest()
            return [self.__client_key_list[cl_id],self.new_key],[self.__serv_key,[self.new_key,cl_id]]
        else:
            return None

    def auth_2(self,serc_name,c,verif):
        print("Second level Authentication")
        if c[0]==self.__serv_key:
            if c[1][1]==verif[1]:
                print("Second level Authorized")
                if serc_name in self.__service_key_list:
                    self.new_key_1=randint(101,1000001)
                    while self.new_key_1 in self.__client_key_list.values():
                        self.new_key_1=randint(101,1000001)
                    self.new_key=xxhash.xxh32(str(c[1][1]),seed=self.new_key_1).hexdigest()
                    return [verif[0],self.new_key],[self.__service_key_list[serc_name],[self.new_key,verif[1]]]
                else:
                    print("No service found!")
                    return None
            else:
                print("Invalid Creds!")
                return None
        else:
            print("Invalid Creds!")
            return None

    def serc_connect(self,serc_name,d,verif,data=None):
        
        print("Third Level Authentication")
        print(serc_name,d,verif)

        if d[0]==self.__service_key_list[serc_name]:
            if d[1][1]==verif[1]:
                print("Third Level Authorized!")
                #self.__service_list[serc_name].check(d[0])
                if data==None:
                    return 1

                
                #Service function
                else:
                    sample_dict={}
                    token_list=[]
                    for i in data:
                        if i not in token_list:
                            sample_dict[i]=1
                            token_list.append(i)
                        else:
                            sample_dict[i]+=1
                    return sample_dict
            else:
                print("Invalid Creds!")
        else:
            print("Invalid Creds!")

        return 0

    
        
          

class Service:
    #use rand 
    def __init__(self,name,passk):
        self.name=name
        self.__serc_id=passk
        self.__key=xxhash.xxh32(str(self.name),seed=self.__serc_id).hexdigest()

        self.__dict={}
        

    def check(self,verif_k):
        if verif_k==self.__key:
            print("Using service "+self.name)

            a=input("Enter Data :")
        else:
            print("Invalid Creds!")


    def temp_print(self):
        print("Name :",self.name)
        print("Service ID :",self.__serc_id)
        print("Service Key :",self.__key)
        
    
#Variables
serv_dict={}
cli_dict={}

   
def create_servers(serv_name):
    #a=input("Enter Server name :")
    serv_dict[serv_name]=Server()

def create_client(client_name):
    if serv_dict=={}:
        return "No servers found!"
    else:
        if client_name in cli_dict:
            return "Client name exists!"
        else:
            cli_dict[client_name]=Client()

            for i in serv_dict:
                serv_dict[i].add_client(cli_dict[client_name].cl_id)
    
   


#####
#Main
create_servers("1")
create_client("test1")
serv_dict["1"].add_services()
serv_dict['1'].temp_print()


