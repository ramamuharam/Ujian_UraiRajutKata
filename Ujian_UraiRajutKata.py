class UraiRajutKata:
    def urai(self, string):
        result = ''
        for i in range(len(string)):
            for j in range(i + 1):
                result += string[j]
        return result

    def rajut(self, string):
        current_len = 1

        while len(string) > 0:
            result = string[:current_len]
            string = string[current_len:]
            current_len += 1

        return result

x = UraiRajutKata()
print(x.urai('Code'))
print(x.urai('Python'))
print(x.urai('Purwadhika'))
print(x.rajut('CCoCodCode'))
print(x.rajut('PPyPytPythPythoPython'))
print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

