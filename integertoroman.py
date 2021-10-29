iclass Solution:
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
        # process flow get thousands, hundreds, tens, ones digits. convert to rn and a
        #append for each digit
        
        if thou > 0:
            print('>t1000')
            for i in range(0,thou):
                    roman += 'M'
        
        if hund > 0:
            print('>t100')
            if hund == 9:
                roman += 'CM'
            elif hund == 8:
                roman += 'DCCC'  
            elif hund == 7:
                roman += 'DCC'    
            elif hund == 6:
                roman += 'DC'
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
                roman += 'L'   
            elif tens == 4:
                roman += 'XL'
            else:
                for i in range(0,tens):
                    roman += 'X'
                    
        if ones > 0:
            print('>t1')
            if ones == 9:
                roman += 'IX'
            elif ones == 8:
                roman += 'VIII'  
            elif ones == 7:
                roman += 'VII'    
            elif ones == 6:
                roman += 'VI'
            elif ones == 5:
                roman += 'V'   
            elif ones == 4:
                roman += 'IV'
            else:
                for i in range(0,ones):
                    roman += 'I'
        return roman
        

