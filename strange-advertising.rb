#!/bin/ruby
#https://www.hackerrank.com/challenges/strange-advertising/problem
#
require 'benchmark'

def viralAdvertising(n, sum = 0)
    n -= 1
    return 5/2, 5/2 if n.zero?
    result, sum =  viralAdvertising(n, sum)
    result = result * 3 / 2
    return result, sum += result
end

def viralAdvertisingIretating(n)
  res = [2]
  (n - 1).times { res << res.last * 3 / 2 }
  res.sum
end

n = gets.strip.to_i
Benchmark.bm do |x|
 x.report { result = viralAdvertising(n).last }
 x.report { result = viralAdvertisingIretating(n) }
end

# puts result
