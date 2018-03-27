#!/bin/ruby
#solution for https://www.hackerrank.com/challenges/encryption/problem

def encryption(s)
  rows = Math.sqrt(s.size).floor
  columns = Math.sqrt(s.size).ceil
  rows = columns if rows * columns < s.size
  columns.times.map do |i|
    rows.times.map do |j|
      s[i + columns * j]
    end.join
  end.join(' ')
end

s = gets.strip.gsub(' ', '')
result = encryption(s)
puts result
