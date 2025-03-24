class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings=sorted(meetings,key=lambda x:x[0])
        empty=0
        lat_end=0
        for st,en in meetings:
            if st>lat_end+1:
                empty+=st-lat_end-1
            
            lat_end=max(lat_end,en)
        
        empty+=days-lat_end
            
        

        return empty
        
        