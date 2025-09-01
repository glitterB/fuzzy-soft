# Fuzzy Logic

[1. Introduction](#1.-Introduction)   
[2. What is Fuzzy set?](#2.-What-is-Fuzzy-set?)  
[3. Fuzzy Operations](#3.-Fuzzy-Operations)   
[4. References](#4.-References)

---


*Prerequisite: Basic understanding of classical set theory.*


# 1. Introduction

### **Classical (Crisp) Set:-**  

A classical set is an **unordered collection** of distinct elements—essentially, a collection of objects.

**Examples:**
- Set of all positive integers  
- Set of all months in a year

Mathematically, a set can be represented as:
$$A = \{~ a,e,i,o,u ~ \}$$

# 2. What is a Fuzzy set?

A fuzzy set is a collection of **ordered pairs**, where each element is associated with a membership value between 0 and 1.

Mathematically, a fuzzy set is represented as:

$$A =\{ (x,\mu_{S}(x)), x\in X\}$$

Where $X$ is an Universal set and $\mu_{S}$ is membership function value.


# 3. Fuzzy Operations

Let A and B be tow fuzzy sets defined on universal set X, then different Fuzzy set operations can be defined as follows,

1. Subset:-  
$$A\subset B \iff \mu_{A}(x)<\mu_{B}(x)$$

2. Equal:-  
$$A= B \iff \mu_{A}(x)=\mu_{B}(x)$$

3. Complement:-  
$$\bar A  = \{ x, 1-\mu_{A}(x)\}$$

4. Union:-  
$$A\cup B = \{ x, max[\mu_{A}(x),\mu_{B}(x)] \}$$

5. Intersection:-  
$$A\cup B = \{ x, min[\mu_{A}(x),\mu_{B}(x)] \}$$

6. Algebric Product:-  
$$A\cdot B = \{ x,\mu_{A}(x)\cdot\mu_{B}(x) \}$$

7. Multiplication by crisp number:-  
$$c\cdot A = \{ x, c\cdot\mu_{A}(x)\}$$

8. p<sup>th</sup> power:-  
$$A^p = \{ x, \mu_{A}(x)^p\}$$

9. Algebraic sum:-  
$$A+B = \{ x,\mu_{A}(x)+\mu_{B}(x) \}$$

10. Algebraic difference:-  
$$A-B = \{ x,\mu_{A}(x)-\mu_{B}(x) \}$$

11. Bounded sum:-  
$$A\oplus B = \{ x,\mu_{A}(x)\oplus \mu_{B}(x) \}$$


$$\mu_{A}(x)\oplus \mu_{B}(x) =min[1,\mu_{A}(x)+\mu_{B}(x)]$$

12. Bounded difference:-  
$$A\ominus B = \{ x,\mu_{A \ominus B}(x)\}$$


$$\\mu_{A \ominus B}(x) =max[0,\mu_{A}(x)+\mu_{B}(x)-1]$$


# 4. References
1. D. K. Pratihar, _Soft Computing_, Narosa Publications, New Delhi, 2008
2. Shridhar Rajendra Mankar, _5 Minute Engineering_, YouTube Channel, 2019