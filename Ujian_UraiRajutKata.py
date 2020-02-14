class UraiRajutKata:
    def urai(self, kata):
        result = ''
        for i in range(len(kata)):
            for j in range(i + 1):
                result += kata[j]
        return result

    def rajut(self, kata):
        current_len = 1

        while len(kata) > 0:
            result = kata[:current_len]
            kata = kata[current_len:]
            current_len += 1

        return result

x = UraiRajutKata()
print(x.urai('Code'))
print(x.urai('Python'))
print(x.urai('Purwadhika'))
print(x.rajut('CCoCodCode'))
print(x.rajut('PPyPytPythPythoPython'))
print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

