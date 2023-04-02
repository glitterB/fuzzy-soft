"""a fuzzy set inplementation using python."""
class FuzzySet():
    
    def __init__(self):
        """Set initialization"""
        self._elements = {}
    
    def __setitem__(self,element,new_mem_value):
        """ Updates/assigns membership value of an element."""
        if new_mem_value>=0 and new_mem_value<=1:
            self._elements[element] = new_mem_value
        else:
            raise ValueError("Membership value shold be in range of 0-1")
        
    def __repr__(self):
        return f"{self._elements.items()}"
    
    def __len__(self):
        return len(self._elements)
    
    def __getitem__(self,element):
        try:
            return self._elements[element]
        except KeyError:
            print("Item does not exists")
    
    def __contains__(self, element):
            return self._elements[element]
    
    def membership_function(self):
        """to be updated later"""
        pass
    
    def append(self,**element):
        """ Adds elemetns in fuzzy set.
            
            Raises value error in element already exits."""
        for key,item in element.items():
            if key in self._elements:
                raise ValueError("Element already exits")
            else:
                if item>=0 and item<=1:
                    self._elements[key] = item
    #Fuzzy Operations
    def complement(self):
        """returns new fuzzy set with complement of two sets"""
        return {i:(1-j) for i,j in self._elements.items()}
            
    def union(self,other):
        """returns new fuzzy set with union of two sets"""
        
        return {i:max(self._elements[i],other._elements[i]) for i in (self._elements.keys())}
    
    def intersection(self,other):
        """returns new fuzzy set with union of two sets"""
        
        return {i:min(self._elements[i],other._elements[i]) for i in (self._elements.keys())}
                
        
if __name__ == "__main__":
    
    a = FuzzySet()
    b = FuzzySet()
    a.append(f=0.1,s=0.35,t=0.55)
    b.append(f=0.9,s=0.65,t=0.45)
    
    b.complement()
    
    
    
