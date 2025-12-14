#Fuzzy set implementation
class FuzzySet():
    
    def __init__(self):
        """Set initialization"""
        self._elements = {}
    def _validate_membership(self, value):
        if not (0 <= value <= 1):
            raise ValueError("Membership value should be in range [0, 1]")
    
    def __setitem__(self,element,val):
        """ Updates/assigns membership value of an element."""
        self._validate_membership(val)
        self._elements[element] = val
        
        
    def __repr__(self):
        return f"FuzzySet({self._elements})"
    
    def __len__(self):
        return len(self._elements)
    
    def __getitem__(self, element):
        return self._elements.get(element, None)

    def __contains__(self, element):
        return element in self._elements
    
    def membership_function(self):
        """to be updated later"""
        pass
    
    def append(self, element, value=None, **elements):
        if value is not None:
            elements[element] = value
        for key, val in elements.items():
            if key in self._elements:
                raise ValueError(f"Element '{key}' already exists")
            self._validate_membership(val)
            self._elements[key] = val

                    
    #Fuzzy Operations
    def subset(self, other):
        """Returns True if a fuzzy set is subset of another."""
        if not isinstance(other, FuzzySet):
            return NotImplemented
        if self._elements.keys() != other._elements.keys():
            return False
        return all(self._elements[k] < other._elements[k] for k in self._elements)

    def __eq__(self, other):
        """Returns True if two fuzzy sets have exactly the same elements and membership values."""
        if not isinstance(other, FuzzySet):
            return NotImplemented
        if self._elements.keys() != other._elements.keys():
            return False
        return all(self._elements[k] == other._elements[k] for k in self._elements)

    
    def complement(self):
        """Returns the complement of this fuzzy set as a new FuzzySet."""
        result = FuzzySet()
        for k, v in self._elements.items():
            result[k] = 1 - v
        return result

            
    def union(self, other):
        """Returns the union of two fuzzy sets as a new FuzzySet."""
        result = FuzzySet()
        keys = set(self._elements.keys()) | set(other._elements.keys())
        for k in keys:
            m1 = self._elements.get(k, 0)
            m2 = other._elements.get(k, 0)
            result[k] = max(m1, m2)
        return result

    def intersection(self, other):
        """Returns the intersection of two fuzzy sets as a new FuzzySet."""
        result = FuzzySet()
        keys = set(self._elements.keys()) & set(other._elements.keys())
        for k in keys:
            m1 = self._elements[k]
            m2 = other._elements[k]
            result[k] = min(m1, m2)
        return result
    
    def __add__(self, other):
        """Returns the algebraic addition of two fuzzy sets as a new FuzzySet."""
        result = FuzzySet()
        keys = set(self._elements.keys()) | set(other._elements.keys())
        for k in keys:
            m1 = self._elements.get(k, 0)
            m2 = other._elements.get(k, 0)
            result[k] = m1+m2-(m1*m2)
        return result
    
    def __sub__(self, other):
        """Returns the algebraic subtraction of two fuzzy sets as a new FuzzySet."""
        result = FuzzySet()
        keys = set(self._elements.keys()) | set(other._elements.keys())
        for k in keys:
            m1 = self._elements.get(k, 0)
            m2 = other._elements.get(k, 0)
            result[k] = m1-m2
        return result
    
    def __mul__(self, other):
        """Returns the multiplication of two fuzzy sets (product t-norm)
        or scalar multiplication with a crisp number."""
        result = FuzzySet()
        
        if isinstance(other, FuzzySet):
            # FuzzySet × FuzzySet
            keys = set(self._elements.keys()) | set(other._elements.keys())
            for k in keys:
                m1 = self._elements.get(k, 0)
                m2 = other._elements.get(k, 0)
                result[k] = m1 * m2
            return result
        
        elif isinstance(other, (int, float)):
            # FuzzySet × scalar
            for k, v in self._elements.items():
                val = v * other
                result[k] = min(max(val, 0), 1)  # clamp into [0, 1]
            return result
    
        return NotImplemented
    def __pow__(self, p):
        """Returns a new FuzzySet with membership values raised to the power p."""
        if not isinstance(p, (int, float)):
            return NotImplemented
        if p < 0:
            raise ValueError("Exponent must be non-negative for fuzzy sets.")
        
        result = FuzzySet()
        for k, v in self._elements.items():
            result[k] = v ** p
        return result
    
    def bdsum (self, other):
        """Returns the bounded sum of two fuzzy sets as a new FuzzySet."""
        result = FuzzySet()
        keys = set(self._elements.keys()) | set(other._elements.keys())
        for k in keys:
            m1 = self._elements.get(k, 0)
            m2 = other._elements.get(k, 0)
            result[k] = min(1,m1+m2)
        return result
    
    def bddiff(self, other):
        """Returns the bounded difference of two fuzzy sets as a new FuzzySet."""
        result = FuzzySet()
        keys = set(self._elements.keys()) | set(other._elements.keys())
        for k in keys:
            m1 = self._elements.get(k, 0)
            m2 = other._elements.get(k, 0)
            result[k] = max(0,m1+m2-1)
        return result
        
#----------------------XoX----------------------
        
if __name__ == "__main__":
    
    a = FuzzySet()
    b = FuzzySet()
    
    a.append("x",0.5,f=0.1,s=0.35,t=0.55)
    b.append("x",0.5,f=0.9,s=0.65,t=0.45)