class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        packed_tuple = zip(timestamp, username, website)
        sorted_packed_tuple = sorted(packed_tuple)  # sort by timestamp, as it didn't say timestamp is sorted array
        
        mapping = defaultdict(list)
        for t, u, w in sorted_packed_tuple:
            mapping[u].append(w)
        
        counter_dict = defaultdict(int)
        
        for website_list in mapping.values():
            combs = set(combinations(website_list, 3))
            
            for comb in combs:
                counter_dict[comb] += 1
        
        sorted_counter_dict = sorted(counter_dict, key=lambda x: (-counter_dict[x], x))
        
        return sorted_counter_dict[0]