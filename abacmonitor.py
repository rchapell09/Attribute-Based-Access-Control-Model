class Attribute():
    type=""
    name=""
class Permission():
    name=""
class Entity():
    name=""
class Policy(object):
    def __init__(self):
        self.conditionlist=[]
    permname=""
class Condition():
    attname=""
    condval=""
class AttributeAss():
    entname=""
    attrname=""
    attvalue=""
import sys

instructionArray=[None]*100
ATTRS_LIST=[]
PERM_LIST=[]
PA_LIST=[]
ENTITY_LIST=[]
AA_LIST=[]



def load_policy(policyfilename):
    fileobj = open(policyfilename, "r")
    ##seperate the ATTRS
    
    attrline =fileobj.readline()
    attrgetridofnewline = "", ""
    if "\n" in attrline:
        attrgetridofnewline = attrline.split('\n')
    else:
        attrgetridofnewline = attrline,""
    attrrhsline=[]
    attrrhsline = attrgetridofnewline[0].split('=')
    attrsvectors=[]
    attrsvectors = attrrhsline[1].split(';')

    attrvectornospace=[]
    for morestuff in attrsvectors:
        if morestuff != "":
            attrvectornospace.append(morestuff)

    attrvectorlist=[]
    for stuff in attrvectornospace:
         if stuff[0] == " ":
             attrvectorlist.append( stuff.split(' <'))
         elif stuff[0] == "<":
             attrvectorlist.append(stuff.split('<'))
    attrsnext=[]
    for things in attrvectorlist:
        attrsnext.append(things[1].split('>'))
    attrslast=[]
    for morethings in attrsnext:
        attrslast.append(morethings[0].split(', '))
    for lastly in attrslast:
        a = Attribute()
        a.type = lastly[0]
        a.name = lastly[1]
        ATTRS_LIST.append(a)
    ##finished ATTRS, about to call print to check if theyre all stored properly
    """
    for item in ATTRS_LIST:
        print("item name:", item.name)
        print("item type:", item.type)
    """
    ##start permline
    
    permline=fileobj.readline()
    permNonewline=[]
    permNonewline = permline.split('\n')
    permRhs=[]
    permRhs = permNonewline[0].split('=')
    permElem=[]
    permElem= permRhs[1].split(';')
    permElemlist = []
    for perm1 in permElem:
        if perm1[0] ==" ":
            permElemlist.append(perm1.split(' <'))
        elif perm1[0] == "<":
            permElemlist.append(perm1.split('<'))
   
    permElemlast= []
    for perm2 in permElemlist:
        permElemlast.append(perm2[1].split('>'))
    for perm3 in permElemlast:
        b = Permission()
        b.name = perm3[0]
        PERM_LIST.append(b)
    
    ##print to check they were added right
    """
    for permitem in PERM_LIST:
        print(permitem.name)
    """

    ## read PA
   
    paline=fileobj.readline()
    paNonewline=[]
    paNonewline = paline.split('\n')
    parhs=[]
    parhs = paNonewline[0].split('=')
    papolicies=[]
    condElem=[]
    cond=[]
    papolicies = parhs[1].split('-')
    for policy in papolicies:
        c = Policy()
        cond = policy.split(':')
        paname = cond[1].split(' ')
        condElem = cond[0].split(';')
        c.permname = paname[1]
        paconditionlist = []
        for condItem in condElem:
            if condItem[0]==" ":
                paconditionlist.append(condItem.split(' <'))
            elif condItem[0]=="<":
                paconditionlist.append(condItem.split('<'))
        condElemnext = []
        for condItem2 in paconditionlist:
            condElemnext.append(condItem2[1].split('>'))
        condElemLast = []
        for condItem3 in condElemnext:
            condElemLast.append(condItem3[0].split(','))
         
        for yuh in condElemLast:
            if yuh[0]!= "" and yuh[0]!=" ":
                ca = Condition()
                ca.attname = yuh[0]
                tempvar = ""
                if yuh[1][0] == " ":
                    tempvar = yuh[1].split(' ')
                    ca.condval = tempvar[1]
                else:
                    ca.condval = yuh[1]

                c.conditionlist.append(ca)
        PA_LIST.append(c)
        

    ##checkif it was stored properly
    """
    for nice in PA_LIST:
        print(nice.permname)
        for nicedude in nice.conditionlist:
            print("name is: ",nicedude.attname)
            print("value is: ",nicedude.condval)
    """
    ##read Entities
    
    entline=fileobj.readline()
    entNonewline = entline.split('\n')
    entrhs = entNonewline[0].split('=')
    entElem=[]
    entElem = entrhs[1].split(';')
    entElemlist = []
    for ent1 in entElem:
        if ent1[0] ==" ":
            entElemlist.append(ent1.split(' <'))
        elif ent1[0] == "<":
            entElemlist.append(ent1.split('<'))
    entLast = []
    for ent2 in entElemlist:
        entLast.append(ent2[1].split('>'))
    for ent3 in entLast:
        d = Entity()
        d.name = ent3[0]
        ENTITY_LIST.append(d)
    ##finished with Entity check if it is loaded right
    """
    for entitem in ENTITY_LIST:
        print(entitem.name)
    """
    ##read aa
    
    aaline=fileobj.readline()
    aaNonewline = aaline.split('\n')
    
    aarhs = aaNonewline[0].split('=')
   
    aaElem = aarhs[1].split(';')
    
    aaElemlist=[]
    for aayuh1 in aaElem:
        
        aaElemlist.append(aayuh1.split(':'))

    fixblanks=[]
   
    for aafixblanks in aaElemlist:
        if aafixblanks!=[""]:
            fixblanks.append(aafixblanks)
        else:
            fixblanks = fixblanks

        
    aaentnamelist=[]
    

    aaAttlist=[]
    
    for aayuh2 in fixblanks:
        if aayuh2[0][0] == " ":
            aaentnamelist.append(aayuh2[0].split(' <'))
        elif aayuh2[0][0]=="<":
            aaentnamelist.append(aayuh2[0].split('<'))
        
        if aayuh2[1][0] == " ":
            aaAttlist.append(aayuh2[1].split(' <'))
        elif aayuh2[1][0] == "<":
            aaAttlist.append(aayuh2[1].split('<'))
  
    aaEntnamelist2 =[]

    for aayuh3 in aaentnamelist:
        aaEntnamelist2.append(aayuh3[1].split('>'))
 
    aaAttlist2 = []
    for aayuh4 in aaAttlist:
        aaAttlist2.append(aayuh4[1].split('>'))
    
    aaAttlist3=[]
    
    for aayuh6 in aaAttlist2: 
        aaAttlist3.append(aayuh6[0].split(', '))
    
    count = 0
   
    for aayuh5 in aaEntnamelist2:
        
        
        
        okay = AttributeAss()
        okay.entname= aayuh5[0]
        tempelement = aaAttlist3[count]
        
        okay.attrname = tempelement[0]
        okay.attvalue = tempelement[1]
        AA_LIST.append(okay)
        count=count+1
    ##check and see if everything was added right
    """
    for AAcheck in AA_LIST:
        print("entName is: ",AAcheck.entname)
        print("attName is: ",AAcheck.attrname)
        print("attValue is: ",AAcheck.attvalue)
    """  

def show_policy():
    print("ATTRS")
    for aitem in ATTRS_LIST:
        print("\t<",aitem.name,",",aitem.type,">")
    print("PERMS")
    for pitem in PERM_LIST:
        print("\t<",pitem.name,">")
    print("PA")
    for paitem in PA_LIST:
        print("\t",paitem.permname)
        for conditem in paitem.conditionlist:
            print("\t\t<",conditem.attname,",",conditem.condval,">")
    print("ENTITIES")
    for enitem in ENTITY_LIST:
        print("\t<",enitem.name,">")
    print("AA")
    for aaaitem in AA_LIST:
        print("\t<",aaaitem.entname,"> <",aaaitem.attrname,",",aaaitem.attvalue,">")



def check_permission(username,objname,envname,permname):
    usernameisEnt=False
    objnameisEnt=False
    envnameisEnt=False
    permnameisPerm=False

    PermGranted=False

    for ent in ENTITY_LIST:
        if ent.name==username:
            usernameisEnt=True
        if ent.name==objname:
            objnameisEnt=True
        if ent.name==envname:
            envnameisEnt=True
    
    for perm in PERM_LIST:
        if perm.name==permname:
            permnameisPerm=True
    
    if usernameisEnt and objnameisEnt and envnameisEnt and permnameisPerm:

        checkcondlist=[]
        for AA in AA_LIST:
            
            if AA.entname==username:
                temp = Condition()
                temp.attname = AA.attrname
                temp.condval = AA.attvalue

                checkcondlist.append(temp)
            elif AA.entname==objname:##more than one possiblity
                """
                hoedontdoit=False
                for enttt in ENTITY_LIST:
                    if enttt.name == AA.attvalue:
                        hoedontdoit=True
                if hoedontdoit==False:
                    temp = Condition()
                    temp.attname =AA.attrname
                    temp.condval = AA.attvalue
                    checkcondlist.append(temp)
                """
                temp = Condition()
                temp.attname =AA.attrname
                temp.condval = AA.attvalue
                checkcondlist.append(temp)

            elif AA.entname==envname:
                temp = Condition()
                temp.attname= AA.attrname
                temp.condval= AA.attvalue

                checkcondlist.append(temp)
                

        for PA in PA_LIST:
            if PA.permname == permname:
                
                truearray=[]
                countofconditions = len(PA.conditionlist)
                for cond in PA.conditionlist:
                    for checkcond in checkcondlist:
                        if cond.attname==checkcond.attname and cond.condval==checkcond.condval:

                            truearray.append(1)
                if len(truearray)==countofconditions:
                    PermGranted=True
        if PermGranted==True:
            print("Permission GRANTED!")
        else:
            print("Permission DENIED!")

        
        
def add_entity(entname):        ##double check this works lol
    isinthelist = False
    for addentity_item in ENTITY_LIST:
        if addentity_item.name == entname:
            isinthelist=True
    if isinthelist==False:
        tempe=Entity()
        tempe.name = entname
        ENTITY_LIST.append(tempe)
        


def remove_entity(entname):
    newENTITY_LIST=[]
    global ENTITY_LIST
    for reeitem in ENTITY_LIST:
        
        if reeitem.name == entname:
            newAA_LIST=[]
            global AA_LIST
            for reattass in AA_LIST:
                if reattass.entname == entname:
                    entname=entname       ##delete from aalist
                elif reattass.attvalue == entname:
                    entname=entname
                else:
                    newAA_LIST.append(reattass)
            AA_LIST=newAA_LIST

            conditionlistcount = 0
            ##remove from PA_LIST
            global PA_LIST
            newPA_LIST=[]
            newCONDlist=[]
            for repaitem in PA_LIST:
                conditionlistcount=len(repaitem.conditionlist)
                
                wehavetodeletethis=False
                for reconditem in repaitem.conditionlist:
                    
                    if reconditem.condval == entname:
                        ##found one in condition list
                        
                        conditionlistcount=conditionlistcount-1    ##delete from item in conditionlist

                        if conditionlistcount == 0:
                            wehavetodeletethis=True    ##its the only condition so delete the whole PA_list item
                    else:
                        newCONDlist.append(reconditem)
                
                if wehavetodeletethis == True:
                    entname=entname
                elif wehavetodeletethis==False:
                    repaitem.conditionlist=newCONDlist
                    newPA_LIST.append(repaitem)
                    newCONDlist=[]
            PA_LIST=newPA_LIST
        else:
            newENTITY_LIST.append(reeitem)
    if ENTITY_LIST!=newENTITY_LIST:
        ENTITY_LIST=newENTITY_LIST



def add_attribute(attrname,attrtype):
    addattributebool = False
    global ATTRS_LIST
    for adat in ATTRS_LIST:
        if adat.name == attrname:
            addattributebool = True
    if addattributebool == False:
        addatt = Attribute()
        addatt.name = attrname
        addatt.type = attrtype
        ATTRS_LIST.append(addatt)


def remove_attribute(attrname):
    newATTRS_LIST=[]
    global ATTRS_LIST
    for rematt in ATTRS_LIST:
        
        if rematt.name == attrname:
                                  ##delete it from the attrslist
            newPA_LIST=[]
            newCONDlist=[]
            global PA_LIST
            for reattinpa in PA_LIST:
                condlistcount = len(reattinpa.conditionlist)
                wehavetodeletethis=False
                
                for reattincondlistel in reattinpa.conditionlist:
                    
                    if reattincondlistel.attname==attrname:
                        condlistcount=condlistcount-1
                        if condlistcount==0:
                            wehavetodeletethis=True 
                    else:
                        newCONDlist.append(reattincondlistel)
                if wehavetodeletethis==True:
                    attrname=attrname
                elif wehavetodeletethis==False:
                    reattinpa.conditionlist=newCONDlist
                    newPA_LIST.append(reattinpa)
                    newCONDlist=[]
            PA_LIST=newPA_LIST

            newAA_LIST=[]
            global AA_LIST
            for reattinaa in AA_LIST:
                if reattinaa.attrname != attrname:
                    newAA_LIST.append(reattinaa)
            AA_LIST=newAA_LIST
        else:
            newATTRS_LIST.append(rematt)
    ATTRS_LIST=newATTRS_LIST

            
def add_permission(permname):
    addpermissionbool = False
    global PERM_LIST
    for permitem in PERM_LIST:
        if permitem.name == permname:
            addpermissionbool=True
    if addpermissionbool==False:
        addperm = Permission()
        addperm.name = permname
        PERM_LIST.append(addperm)
    
def remove_permission(permname):
    newPERM_LIST=[]
    global PERM_LIST
    for repermitem in PERM_LIST:
        if repermitem.name == permname:
            newPA_LIST=[]
            global PA_LIST
            for repermiteminpa in PA_LIST:
                if repermiteminpa.permname == permname:
                    permname=permname
                else:
                    newPA_LIST.append(repermiteminpa)
            PA_LIST=newPA_LIST
        else:
            newPERM_LIST.append(repermitem)
    PERM_LIST=newPERM_LIST

def add_attributes_to_permission(permname, attlist):##tricky one hwere it can recieve an array of pairs

    times=0
    timesis0orbad=False
    isapermission = False
    for permitemm in PERM_LIST:
        if permitemm.name == permname:
            isapermission=True
    
    

    if len(attlist)!=0:
        if (len(attlist)%2)==0:
            times=len(attlist)/2
        else:
            timesis0orbad=True
    else:
        timesis0orbad=True
    

    if timesis0orbad==False:
        global PA_LIST
        global ATTRS_LIST
        if isapermission==True:

            newPA = Policy()
            newPA.permname=permname
    
            i=0
            j=1
            while times>0:
            
                isavalidAttname=False
                for attn in ATTRS_LIST:
                    if attn.name == attlist[i]:
                        isavalidAttname=True
            
                if isavalidAttname==True:

                    cond = Condition()
                    cond.attname = attlist[i]##check that its valid already?
                    cond.condval = attlist[j]##Check that its valid alread?
                    newPA.conditionlist.append(cond)
                i=i+2
                j=j+2
                times=times-1
            if (len(newPA.conditionlist)!=0):
                PA_LIST.append(newPA)
             
    
        
   
            
def remove_attribute_from_permission(permname,attrname,attrvalue):
    newPA_LIST=[]
    global PA_LIST
    for reattfromperm in PA_LIST:
        wehavetodeletethis=False
        
        if reattfromperm.permname == permname:
            newCondlist = []
            condcount = len(reattfromperm.conditionlist)
            for conditem in reattfromperm.conditionlist:
                if conditem.attname==attrname and conditem.condval == attrvalue:
                    condcount=condcount-1
                    if condcount==0:
                        wehavetodeletethis=True
                else:
                    newCondlist.append(conditem)
            reattfromperm.conditionlist=newCondlist
        if wehavetodeletethis==False:
            newPA_LIST.append(reattfromperm)
    PA_LIST=newPA_LIST



def add_attribute_to_entity(entname,attrname,attrval):
    global ENTITY_LIST
    global ATTRS_LIST
    global AA_LIST
    isinentlist = False
    isinattlist=False
    for entitem in ENTITY_LIST:##checking the values are there
        if entitem.name==entname:
            isinentlist=True
    for attrsitem in ATTRS_LIST:
        if attrsitem.name ==attrname:
            isinattlist=True
    if isinentlist and isinattlist:
        newAAitem = AttributeAss()
        newAAitem.entname=entname
        newAAitem.attrname = attrname
        newAAitem.attvalue = attrval
        AA_LIST.append(newAAitem)



    
def remove_attribute_from_entity(entname,attrname,attrval):
    newAA_LIST=[]
    global AA_LIST
    for aaitem in AA_LIST:
        if aaitem.entname == entname and aaitem.attrname==attrname and aaitem.attvalue==attrval:
            entname=entname
        else:
            newAA_LIST.append(aaitem)
    AA_LIST=newAA_LIST




def main():
    instruct=[]
    
    inputstring = sys.argv[1]
   
    input_split=inputstring.split(';')
    i=0
    for command in input_split:##figureout instructions
        instruct = command.split(' ')
        instructionVal=[]
        for val in instruct:
            if val != "":
                instructionVal.append(val)      
        instructionArray[i] = instructionVal
        i=i+1

    for j in range(0,i):##execute instructions
        call = instructionArray[j]
        function = call[0]
        
        if function == "show-policy":
            show_policy()
        elif function == "load-policy":
            load_policy(call[1])
        elif function == "add-entity":
            add_entity(call[1])
        elif function == "remove-entity":
            remove_entity(call[1])
        elif function == "add-attribute":
            add_attribute(call[1],call[2])
        elif function == "remove-attribute":
            remove_attribute(call[1])
        elif function == "add-permission":
            add_permission(call[1])
        elif function == "remove-permission":
            remove_permission(call[1])
        elif function == "add-attributes-to-permission":
           
            count=0
            atlist=[]
            for item in call:
                if count==0:##this is call[0] which is funciton
                    count=1
                elif count==1:##this is call[1] which is permname
                    count=2
                elif count==2:##this is call[2..4..6..8]
                    count=3
                    atlist.append(item)
                    
                elif count==3:
                    count=2
                    atlist.append(item)
           
            add_attributes_to_permission(call[1], atlist)

        elif function == "remove-attribute-from-permission":
            
            remove_attribute_from_permission(call[1],call[2],call[3])
        elif function == "add-attribute-to-entity":
            
            add_attribute_to_entity(call[1],call[2],call[3])
        elif function == "remove-attribute-from-entity":
            
            remove_attribute_from_entity(call[1],call[2],call[3])
        elif function == "check-permission":
            
            check_permission(call[1],call[2],call[3],call[4])
        


    










if __name__ == '__main__':
    main()