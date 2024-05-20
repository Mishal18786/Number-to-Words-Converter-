import time
from dictionary import words,operator
class num_to_words:
    _instance=None
    _cache = {}

    def __new__(cls, *args, **kwargs):
        '''Singleton method'''
        if not cls._instance:
            '''if there is no instance create one'''
            cls._instance = super().__new__(cls)
            '''assigning Dictionary'''
            cls._instance.words = words
        return cls._instance

    @staticmethod
    def convert(n):
        try:
            start = time.time()
            if n in num_to_words._cache:
                return num_to_words._cache[n]

            if n == 0:
                result = ' Zero '
            elif n < 100:
                result = num_to_words._lessthanhundred(n)
            elif n >= 100 and n < 1000:
                result = num_to_words._greaterthanhundred(n)
            elif n >= 1000 and n < 100000:
                result = num_to_words._greaterthanthousand(n, 1000, 'Thousand')
            elif n >= 100000 and n < 10000000:
                result = num_to_words._greaterthanthousand(n, 100000, 'Lakh')
            elif n >= 10000000:
                result = num_to_words._greaterthanthousand(n, 10000000, 'Crore')

            num_to_words._cache[n] = result
            return result
        except (ValueError, Exception) as e1:
            print('invalid Input Enter only Numbers', e1)

    @staticmethod
    def _lessthanhundred(n):
        if n in num_to_words._instance.words:
            return num_to_words._instance.words.get(n)
        else:
            quotient, remainder = divmod(n, 10)
            quotient1 = num_to_words._instance.words.get(quotient * 10)
            remainder1 = num_to_words._instance.words.get(remainder)
            return f'{quotient1} {remainder1}'

    @staticmethod
    def _greaterthanhundred(n):
        quotient, remainder = divmod(n, 100)
        quotient = num_to_words._instance.words.get(quotient)
        if remainder == 0:
            return f"{quotient} Hundred"
        else:
            remainder = num_to_words._lessthanhundred(remainder)
            return f"{quotient} Hundred {remainder}"
    @staticmethod
    def _greaterthanthousand(n, number, unit):
        quotient, remainder = divmod(n, number)
        quotient = num_to_words.convert(quotient)
        if remainder == 0:
            return f"{quotient}  {unit}"
        else:
            remainder = num_to_words.convert(remainder)
            return f"{quotient}  {unit}  {remainder}"

class fasade_numtowords:
    '''Fasade method'''
    def __init__(self):
        self.numtowords_instance=num_to_words()
    def converting_to_word(self,num):
        return self.numtowords_instance.convert(num)



if __name__ == "__main__":
    Fasade = fasade_numtowords()
    while True:
        l = input('Enter a Number to convert to words or "q" to exit:>>>>>')
        if l.lower() == 'q':
            break
        try:
            start = time.time()
            if '.' in l:
                before, after = l.split('.')
                decimals = ' '.join(words.get(int(i)) for i in after)
                before_str = 'Zero' if before == '' else 'Zero' if before in operator else Fasade.converting_to_word(abs(int(before)))

                if l[0] == '-':
                    print(f'{operator[l[0]]} {before_str} {operator["."]} {decimals}')
                else:
                    print(f'{before_str} {operator["."]} {decimals}')
            elif l[0] == '-':
                print(f'{operator[l[0]]} {Fasade.converting_to_word(abs(int(l)))}')
            else:
                print(Fasade.converting_to_word(int(l)))
            print(f'Execution Time: {time.time()-start:.5f} seconds') #execution time
        except (ValueError, TypeError) as v:
            print('you have entered a invalid value enter only numbers \n')