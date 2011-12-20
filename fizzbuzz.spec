from fizzbuzz import *
from fixture import sample_data

set up
    fizzbuzz = FizzBuzz()

acceptance correct 20 first lines
    app = FizzBuzzApp()
    lines = app.run(20)
    lines == sample_data

filter returns 1 for 1
    val = fizzbuzz.filter(1)
    val == "1"

filter returns 2 for 2
    val = fizzbuzz.filter(2)
    val == "2"

filter returns fizz for 3
    val = fizzbuzz.filter(3)
    val == "Fizz"

filter returns buzz for 5
    val = fizzbuzz.filter(5)
    val == "Buzz"

filter returns fizz for 6
    val = fizzbuzz.filter(6)
    val == "Fizz"

filter returns fizzbuzz for 15
    val = fizzbuzz.filter(15)
    val == "FizzBuzz"

filter raises exception for minus values
    fizzbuzz.filter(-1) raises ValueError

filter raises exception for zero
    fizzbuzz.filter(0) raises ValueError


