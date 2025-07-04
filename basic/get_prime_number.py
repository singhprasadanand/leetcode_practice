"""
Problem: Check if a Number is Prime

Intuition:
A number is **prime** if it is greater than 1 and has no positive divisors other than 1 and itself.

We only need to check for factors up to sqrt(n)

Edge Cases:
- 0 and 1 are not prime.
- 2 and 3 are prime.
- Negative numbers are not prime.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def get_prime_number(n:int)->list[int|None]:
    if n <=1:
        return []
    return [i for i in range(2,n+1) if all(i%j!=0 for j in range(2,int(i**0.5)+1))]


def check_is_prime(n:int)->bool:
    if n<=1:
        return False
    return all(n%i!=0 for i in range(2,int(n**0.5)+1))


if __name__ == "__main__":
    print(get_prime_number(20))
    print(check_is_prime(10))