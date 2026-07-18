class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.hashmap:
            return ''

        li = self.hashmap[key]
        n=len(li)
        i,j=0,n-1
        ans=''

        while i<=j:
            mid = i+(j-i)//2
            if li[mid][1]<=timestamp:
                ans=li[mid][0]
                i=mid+1
            else:
                j=mid-1
        return ans