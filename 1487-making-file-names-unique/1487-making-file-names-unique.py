class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        """
        Brut force solution
        """
        
        frequency = dict()

        for i in range(len(names)):
            # Store the current frequency in dict
            frequency[names[i]] = frequency.get(names[i], 0) + 1
            
            if frequency[names[i]] > 1:
                while f"{names[i]}({str(frequency[names[i]]-1)})" in frequency:
                    frequency[names[i]] += 1
                    
                    
                names[i] = f"{names[i]}({str(frequency[names[i]]-1)})"
                frequency[names[i]] = 1
               

        return names  
        