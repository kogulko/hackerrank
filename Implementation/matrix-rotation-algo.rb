#https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

require 'benchmark'

def add_index(arr, i, j)
  arr << { i: i, j: j }
end


def get_indexes(offset, n, m)
  arr = [{ i: (1 + offset), j: (1 + offset) }]

  #left
  while arr.last[:j] < (m - offset)
    add_index(arr, arr.last[:i], arr.last[:j] + 1)
  end

  #down
  while arr.last[:i] < (n - offset)
    add_index(arr, arr.last[:i] + 1, arr.last[:j])
  end

  #right
  while arr.last[:j] > (1 + offset)
    add_index(arr, arr.last[:i], arr.last[:j] - 1)
  end

  #up
  while arr.last[:i] > (2 + offset)
    add_index(arr, arr.last[:i] - 1, arr.last[:j])
  end
  arr
end


def rotate(matrix, n, m, r)
  rotated = Array.new(n) { Array.new(m) }
  [n/2 + n%2, m/2 + m%2].min.times do |offset|
    indexes = get_indexes(offset, n, m)

    values = indexes.map { |index| matrix[index[:i] - 1][index[:j] - 1] }
    (r % values.size).times { values.push(values.shift) }
    indexes.each_with_index do |value, index|
      rotated[value[:i] - 1][value[:j] - 1] = values[index]
    end
  end

  return rotated.map { |i| i.join(' ') }
end

r = 10000
n = 250
m = 250
a = Array.new(n) { Array.new(m) { rand(1..10) } }

puts "ROTATE #{r} times"
Benchmark.bmbm do |x|
   x.report {  puts rotate(a,n,m,r)  }
end
