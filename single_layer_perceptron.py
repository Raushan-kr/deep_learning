#program in python for single layer perceptron by Raushan kumar
#function for find actual output which is weight transpose *input
def out(input1,weight):
    temp = len(weight)
    actual_out=0
    for i in range(0,temp):
        #in actual we have to take transpose of weight vector but for
        #1-D array it will work.
       
        actual_out += int(input1[i])*int(weight[i])
   
    if actual_out>0:
        return 1
    else:
        return 0
        
        
    
    
#function for training the computer
def Train1(input1,temp_weight,desired_out,epoch):
    weight = temp_weight
    actual_out=0
    temp = len(input1)
   
    count =0
    print("epoch",epoch)
    for i in range (0,temp):
        actual_out = out(input1[i] ,weight)
        
        if(actual_out == desired_out[i]):
           
            count += 1
            
        else:
            
            error=desired_out[i]-actual_out
            
            
            del_weight=[]
            for j in input1[i]:
               
                del_weight.append(error*j)
            
            twmp=[]   
            for j in range(0,len(weight)):
                twmp.append(weight[j]+del_weight[j])
              
            print(weight ,' ', input1[i], ' ', desired_out[i] , ' ' ,  actual_out,' ',del_weight,' ',twmp)
            weight = twmp
                
            
            
    if count == temp:
        print(weight)
        #return(weight)
    else:
        Train1(input1,weight,desired_out,epoch+1)

input1=[[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
desired_out=[0,0,0,1]
weight=[0,0,0]
print("weight(n+1)   input  desired_out  actual_out  del_weight  weight(n+1)")
Train1(input1,weight,desired_out,0)

    
