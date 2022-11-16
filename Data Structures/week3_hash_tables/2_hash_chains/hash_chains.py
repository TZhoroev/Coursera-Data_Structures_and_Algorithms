# python3
from collections import defaultdict


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = query[1]
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, buckets_count):
        self.bucket_count = buckets_count
        self.elements = defaultdict(lambda: [])

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            ans = self.elements[query.ind]
            print(" ".join(ans))
        else:
            number = str(self._hash_func(query.s))
            if query.type == "find":
                print("yes" if query.s in self.elements[number] else "no")
            elif query.type == "add":
                if query.s not in self.elements[number]:
                    self.elements[number] = [query.s] + self.elements[number]
            else:
                if query.s in self.elements[number]:
                    self.elements[number].remove(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
