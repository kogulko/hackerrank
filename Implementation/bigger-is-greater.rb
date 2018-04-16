#!/bin/ruby
#solutin for https://www.hackerrank.com/challenges/bigger-is-greater/problem
# Algorithm:
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
#Condensed mathematical description:

# Find largest index i such that array[i − 1] < array[i].
# (If no such i exists, then this is already the last permutation.)

# Find largest index j such that j ≥ i and array[j] > array[i − 1].

# Swap array[j] and array[i − 1].

# Reverse the suffix starting at array[i].
def biggerIsGreater(w)
  pivot = nil
  laggest_sufix = w.size - 1

  1.upto(w.size - 1) do |i|
    pivot = i - 1 if w[i] > w[i-1]
  end

  return 'no answer' unless pivot

  pivot.upto(w.size - 1) do |j|
    laggest_sufix = j if w[j] > w[pivot]
  end

  w[pivot] = w[laggest_sufix].tap { w[laggest_sufix] = w[pivot] }

  w[0..pivot] + w[(pivot + 1)..-1].reverse

    # Complete this function
end

t = gets.strip.to_i
t.times do
    w = gets.strip
    result = biggerIsGreater(w)
    puts result
end
