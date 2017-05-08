def list(*n):
        def gcdtwo(a,b):                   
                if min(a,b) == 0:              
                        return max(a,b)
                return gcdtwo(b,a%b)            
        def gcd(a):                        
                b=gcdtwo(max(a),min(a))        
                a.remove(min(a))               
                a.remove(max(a))                
                a.append(b)                   
                if max(a)==min(a):             
                        print('최대공약수는 : ',a[0]) 
                else:
                        gcd(a)                    
        a = []
        for i in n:
                a.append(i)
        return gcd(a)                         
                                   
if __name__=="__main__":
        list(100,25,20,5)