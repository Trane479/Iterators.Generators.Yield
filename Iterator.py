
def writer(country_name):
    with open('countries.txt', 'a', encoding='utf-8') as file:
        file.write(f'{country_name} - ' 
                   f"https://en.wikipedia.org/wiki/{country_name} \n")


class CountryIterator:

    def __init__(self, start, end, data):
        self.start = start - 1
        self.end = end
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        writer(self.data[self.start]['name']['official'])
        if self.start == self.end:
            raise StopIteration
        return self.start
