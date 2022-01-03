class Underscore:
    def map(self, iterable, callback):
        mapped=[]
        for item in iterable:
            mapped.append(callback(item))
        return mapped
    def find(self, iterable, callback):
        for item in iterable:
            if callback(item):
                return item
    def filter(self, iterable, callback):
        filtered=[]
        for item in iterable:
            if callback(item):
                filtered.append(item)
        return filtered
    def reject(self, iterable, callback):
        admitted=[]
        for item in iterable:
            if not callback(item):
                admitted.append(item)
        return admitted

_=Underscore()