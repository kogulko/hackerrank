#!/bin/ruby
#solution for https://www.hackerrank.com/challenges/sherlock-and-squares/problem

def squares(a, b)
    Math.sqrt(b).floor - Math.sqrt(a).ceil + 1
end

q = gets.strip.to_i
for a0 in (0..q-1)
    a, b = gets.strip.split(' ')
    a = a.to_i
    b = b.to_i
    result = squares(a, b)
    puts result
end
