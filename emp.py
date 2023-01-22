 
import json 

x={   
"emp_details": [
{
"emp_name": "prashansha",
 "DOB":"05/07/1999",
 "height":"5.2",
 "city":"jagdalpur",
"state":"chattisgarh"
},
{ 
        "emp_name": "pankaj",
          "DOB":"10/05/1997",
           "height":"5.5",
           "city" :"raipur",
           "state" :"chattisgarh"
},
     {
          "emp_name": "ram",
           "DOB":"10/12/1997",
           "height":"5.8",
           "city":"delhi",
           "state":"haryana uttar pradesh"
     },
     {
          "emp_name": "shreya",
         "DOB":"11/08/1994",
          "height":"5.7",
         "city":"lucknow",
          "state":"uttarpradesh"
     },
     {
         "emp_name": "vanshika",
         "DOB":"13/02/1992",
         "height":"5.4",
        "city":"hyderbad",
        "state":"telengana"
     } 
 
]
}
with open("emp.json",'w') as f:
    json.dump(x,f,indent=5)
    print("json file generated")

     