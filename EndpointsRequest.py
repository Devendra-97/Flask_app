from backend import *
from model import *
def add_new_question():
    Question_payload=api.payload
    ques_status= ""
    k=ques_collection.find().count()+1
    k=str(k)
    j=ques_collection.insert({"_id":k})
    z=ques_collection.update({"_id":k},Question_payload)
    if z:
        return True
    else:
        return False

def add_new_answer():
    ans_status=""
    answer_payload=api.payload
    k=ans_collection.find().count()+1
    k=str(k)
    j=ans_collection.insert({"_id":k})
    y=ans_collection.update({"_id":k},answer_payload)
    if y:
        return True
    else:
        return False    

def get_all():
    all=[]
    quest=json.loads(dumps(ques_collection.find()))
    ans=json.loads(dumps(ans_collection.find({},{"_id":False})))    
    for i in range(0,len(quest)):
	    question = quest[i]
	    question["answers"] = []
	    for j in range(0,len(ans)):
		    if ans[j]["qid"]==question["_id"]:
			    question["answers"].append(ans[j])        
    all.append(quest)
    ns1.logger.debug("Get all the Entries")   
    return quest



def search_by_id(_id):
    qid=_id
    print(qid)
    logging.getLogger(_id)
    #all=[]
    #ans_collection.find().count()
    t=ques_collection.find().count()
    t=str(t)
    if(qid<=t):
        quest=json.loads(dumps(ques_collection.find({"_id":_id})))
        ans=json.loads(dumps(ans_collection.find({"qid":qid})))
        question=quest[0]
        question["answers"]=[]
        for j in range(0,len(ans)):
            if ans[j]["qid"]==question["_id"]:
                question["answers"].append(ans[j])
        #all.append(quest)
        
        return quest[0]
    else:

        return ("Please Enter Correct Id") 

def search_by_topic():
    l=[]
    v=[]
    new_l1=[]
    p=[]
    all=[]
    k=eval(dumps(api.payload))        
    for i in k.values():            
        l.append(i)
    q1=l[0]
    q1=list(q1)
        #print(l,q1)        
    for i in range (0,len(q1)):
        output=ques_collection.find({"topic":q1[i]})
        k=json.loads(dumps(output))
        v.append(k)
        #print(v)   
    for i in range (0,len(v)):
        new_l1.append(v[i][0])
        #print(v[i][0])
    for i in range (0,len(new_l1)):
        p.append(new_l1[i]["_id"])
    p=set(p)
    p=list(p)    
   
    for i in range(0,len(p)):
        
        ans=json.loads(dumps(ans_collection.find({"qid":p[i]})))
        quest=json.loads(dumps(ques_collection.find({"_id":p[i]})))
        question=quest[0]
        question["answer"]=[]
        for j in range(0,len(ans)):
            question["answer"].append(ans[j])
        all.append(quest)
    ns1.logger.info("You are searching by Topic")
    return all

    

