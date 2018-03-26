#!/bin/ruby
#solution for https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem problem

def organizingContainers(container)
    res1 = container.each_index.map do |i|
        container.each_index.map do |j|
            container[j][i]
        end.sum
    end.sort

    res2 = container.map(&:sum).sort

    res1 == res2 ? 'Possible' : 'Impossible'
    # Complete this function
end

q = gets.strip.to_i
for a0 in (0..q-1)
    n = gets.strip.to_i
    container = Array.new(n)
    for container_i in (0..n-1)
        container_t = gets.strip
        container[container_i] = container_t.split(' ').map(&:to_i)
    end
    result = organizingContainers(container)
    puts result
end
