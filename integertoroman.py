class Solution:
    def get_digit(number, n):
        return number // 10**n % 10
    
    def intToRoman(self, num: int) -> str:
        roman = ''
                
        thou = Solution.get_digit(num, 3)
        hund = Solution.get_digit(num, 2)
        tens = Solution.get_digit(num, 1)
        ones = Solution.get_digit(num, 0)

        print( num)
        #I is 1
        #V is 5
        #X is 10
        #L is 50
        #C is 100
        #D is 500
        #M is 
        #1 to 3999
        # process flow from ones to 5s  tens to 50s to hundreds 5o 500 to 1000
        
        if thou > 0:
            print('>t1000')
            for i in range(0,thou):
                    roman += 'M'
        
        if hund > 0:
            print('>t100')
            if hund == 9:
                roman += 'CM'
            elif hund == 8:
                roman += 'DXXX'  
            elif hund == 7:
                roman += 'DXX'    
            elif hund == 6:
                roman += 'DX'
            elif hund == 5:
                roman += 'D'   
            elif hund == 4:
                roman += 'CD'
            else:
                for i in range(0,hund):
                    roman += 'C'
            
        if tens > 0:
            print('>t10')
            if tens == 9:
                roman += 'XC'
            elif tens == 8:
                roman += 'LXXX'  
            elif tens == 7:
                roman += 'LXX'    
            elif tens == 6:
                roman += 'LX'
            elif tens == 5:
                roman += 'D'   
            elif tens == 4:
                roman += 'XD'
            else:
                for i in range(0,tens):
                    roman += 'X'
                    
        if ones > 0:
            print('>t1')
            if tens == 9:
                roman += 'IX'
            elif tens == 8:
                roman += 'VIII'  
            elif tens == 7:
                roman += 'VII'    
            elif tens == 6:
                roman += 'VI'
            elif tens == 5:
                roman += 'V'   
            elif tens == 4:
                roman += 'iV'
            else:
                for i in range(0,tens):
                    roman += 'I'
        
        if num <=5:
            print('lt5')
            if num == 4:
                roman += 'IV'
            elif num == 5:
                roman += 'V'
            else:
                for i in range(0,num):
                    roman += 'I'
                    
        elif num <= 10:
            print('lt10')
            if num == 9:
                roman += 'IX'
            elif num == 10:
                roman += 'X'
            else:
                roman += 'V'
                for i in range(0,int(num/10)):
                    roman += 'I'
                    
        elif num <=50:
            print('lt50')
            if num == 40:
                roman += 'XL'
            elif num == 50:
                roman += 'L'
            else:
                for i in range(0,(int(num/10))):
                    roman += 'X'
                    
        elif num <= 100:
            print('lt100')
            if num == 90:
                roman += 'XC'
            elif num == 100:
                roman += 'C'
            else:
                roman += 'L'
                for i in range(0,int((num-50)/10)):
                    roman += 'X'   
                    
                    
        elif num <=500:
            print('lt500')
            if num == 400:
                roman += 'CD'
            elif num == 500:
                roman += 'D'
            else:
                for i in range(0,int((num)/100)):
                    roman += 'C'
            
        elif num <= 1000:
            print('lt1000')
            if num == 900:
                roman += 'CM'
            elif num == 1000:
                roman += 'M'
            else:
                roman += 'D'
                for i in range(0,int((num-500)/100)):
                    roman += 'C'


        return roman
        

