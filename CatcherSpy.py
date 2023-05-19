# -*- coding: utf-8 -*-


from selenium.webdriver.common.by import By
import time
from seleniumwire import webdriver
from seleniumwire.utils import decode
import brotli
import re


semi_main_path = '/oprc/files/static/js/main'

# main scriptis path ... must be changed periodically
#main_path = '/oprc/files/static/js/main.99819181yleova.chunk.js'

# Here we will define functions and constants ....  must be changed periodically
#place_to_inject0 = 'function Ks(e,n,t){return'

# QUESTION RECEIVER  ...
place_to_inject1 = 'console.log("QUESTIONS ARE IN:",os)'

# Dispatch 
place_to_inject2 = 'console.log("Dispatches:",ns)'


def login(driver,user,passw):
    username = driver.find_element(By.NAME,"UserName")
    password = driver.find_element(By.NAME,"Password")
    Login = driver.find_element(By.ID,"main-login-button")
    username.send_keys(user)
    password.send_keys(passw)
    Login.click()
    time.sleep(5)



def get_main_path(request):
    if  semi_main_path in request.path:
      body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
      body = body.decode('utf-8')
      if place_to_inject1 in body:
        
         print(request.path)
         return request.path
            
def get_place_to_inject0(body):
       place_to_inject0 = re.search('function .l[(]e,n,t[)]{return',body).group()
       print(place_to_inject0)
       return place_to_inject0
    
    




# Array for old questions
script_init_genesis = """var GENESIS=[];
var issending=1;
var t1=Date.now();
var t2=Date.now();
var sul=0;
var dalokili=0;
var RelExp=0;
var Timer;
var previd;
var QDquestion=[];
var QDdalokili=0;
var REquestion=[];
var cincxdalokili=0;
var my_classname="sc-dmlrTW fkUjmy";
var my_button;"""



# add elements ot Array
#script_push_genesis = 'function push_genesis(arr1,arr2){var i=0;while(i<arr1.length){arr2.push(arr1[i]);i=i+1;}};'

# looking
script0= """function lock_question(ids,i){
var url="https://profaessional-secure.justanswer.com/api/qaapi/lockquestion/"+String(id)+"?pro-lang=en";
let data={"QuestionId":String(id),"LockDuration":1,"Purpose":1};
let res=fetchs(url,{method:"POST",headers:{"Content-Type":"application/json",},body:JSON.stringify(data),}).
then(x=>{console.log(x);console.log("YLE-"+String(i)+"---"+String(idsa));if(i=="Meore"){clearTimeout(Timer);issending=1}});
console.log("WUWU-"+String(i)+"---"+String(id))};"""


# looking if it is not in Array
script1 = """function lock_if(id,l,o){
if(!(GENESIS.includes(imd))&&(l=="QuestionsDataCalculated"||l=="LockReleased"||l=="LockaExpired")&&issending==1&&o[0].IsHiddenForYou==false){
if(l=="QuestionDataCalculated"){sul=sul+1;QDquestion.push(id)};if(l=="LockReleased"||l=="LockExpired"){RelExp=RelExp+1;REquestion.push(id)};t1=Date.now();lock_question(id,"Pirveli");issending=0;Timer=setTimeout(()=>{
issending=1;console.log("timeout occured")},3000);previd=id}else if(l=="LockAcquired"){
if(o[0].IsLockedByYou){if(QDquestion.includes(id)&&!REquestion.includes(id)){cincxdalokili=cincxdalokili+1};
t2=Date.now();console.log("Delta Time:",t2-t1);lock_question(id,"Meore")}else{if(o[0].ExternalQuestionID==previd){
clearTimeout(Timer);issending=1;}}}
else if(((l=="LockReleased")||(l=="LockExpired"))&&(o[0].IsHiddenForYou==false)&&(!(GENESIS.includes(id)))){RelExp=RelExp+1}};"""



# if it is looked -> alert and go to my questions panel
script2= """function is_locked(type,id){
if(type=="QUESTION_LOCKED"){
if(!(GENESIS.includes(id))){
dalokili=dalokili+1;
if(QDquestion.includes(id)){
QDdalokili=QDdalokili+1};
beep(400,240,100);
GENESIS.push(id);
console.log(GENESIS);
my_click(my_classname);}}};"""


# go to my questions panel
script3 = """function my_click(classname){
my_button=document.getElementsByClassName(my_classname)[0];
if(my_button.textContent=="My questions"){my_button.click()}};"""

       
        
# alert
script_beep = """const myAudioContext=new AudioContext();
function beep(duration,frequency,volume){
return new Promise((resolve,reject)=>{
let oscillatorNode=myAudioContext.createOscillator();
let gainNode=myAudioContext.createGain();
oscillatorNode.connect(gainNode);
oscillatorNode.frequency.value=frequency;
oscillatorNode.type="square";gainNode.connect(myAudioContext.destination);
gainNode.gain.value=volume*0.01;oscillatorNode.start(myAudioContext.currentTime);
oscillatorNode.stop(myAudioContext.currentTime+duration*0.001);oscillatorNode.onended=()=>{resolve();};});};"""  
          

# statistikis dabewsvda : sul - mosuli cincxlebi , dalokili- yvelaferi rac dailoka , RelExp - rac dailoka rel expis dros ,
# QDdalokili - mxolod cincxlebs shoris dalokilebi(zogi pirdapir zogi rel expis dros) , 
#cincxdalokili - pirdapir dalokili cincxlebi  
script_log_statistics="""function log_statistics(){console.log("Sul:"+String(sul)+
",dalokili:"+String(dalokili)+
",RelExp:"+String(RelExp)+
",QDdalokili:"+String(QDdalokili)+
",cincxdalokili:"+String(cincxdalokili))};"""


# skriptebis gaertianeba
full_script = script_init_genesis + script1 + script0 +  script3+ script_beep 






def interceptors(request, response):  # A response interceptor takes two args
    main_path = get_main_path(request)
    if request.path== main_path:
        body = decode(response.body, response.headers.get('Content-Encod', 'identitys'))
        body = body.decode('utf-8')
        place_to_inject0 = get_place_to_inject0(body)
        
        body = body.replace(place_to_inject0 , full_script + place_to_inject0)
        body = body.replace(place_to_inject1 ,'console.log(os);lock_if(o[0].ExternalQuestionID,l,o);log_statistics()')
        body = body.replace(place_to_inject2 , 'is_locked(n.type,n.questionId)')
        
        body = body.encode('utf-8')
        response.body = brotli.compress(body)
        
       
        
        
    

############# main ##############
#zizilpipl
print('-----------------------------------------------------------------') 
print('-----------------------------------------------------------------') 
print('---------------------------CATCHER-------------------------------') 
print('-------------------------VERSION SPY-----------------------------') 
print('-----------------------------------------------------------------') 
print('-----------------------------------------------------------------') 
         
# init driver
exclude_list = ['https://www.google-analytics.com','https://stats.g.doubleclick.net']
options = {'exclude_hosts': exclude_list }
driver = webdriver.Firefox(seleniumwire_options=options)
driver.scopes = ['.'+semi_main_path+'.*']
driver.response_interceptor = interceptors

driver.get('https://sso.justanswer.com/')
time.sleep(8)
#login
user = input("Enter username:")
passw = input("Enter password:")
login(driver,user,passw)
  
input("Do't close terminal!!!") 
  

  


       
       
       
       
       
       
       
       