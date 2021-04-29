from transformers import pipeline
import time


def question_hugging():
    start = time.time()
    nlp = pipeline("question-answering")
    context = r"""
The property of being prime (or not) is called primality.
A simple but slow method of verifying the primality of a given number n is known as trial division.
It consists of testing whether n is a multiple of any integer between 2 and itself.
Algorithms much more efficient than trial division have been devised to test the primality of large numbers.
These include the Miller–Rabin primality test, which is fast but has a small probability of error, and the AKS primality test, which always produces the correct answer in polynomial time but is too slow to be practical.
Particularly fast methods are available for numbers of special forms, such as Mersenne numbers.
As of January 2016, the largest known prime number has 22,338,618 decimal digits.
"""
    result = nlp(question="What is a simple method to verify primality?", context=context)
    print(f"Answer: '{result['answer']}'")
    print("Time taken:", time.time() - start, " seconds")


question_hugging()
