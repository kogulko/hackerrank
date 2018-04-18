#solution for https://www.hackerrank.com/challenges/larrys-array/problem
#
#
#https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
def larrysArray(a)
  a.each_index.map do |i|
     ((i+1)..(a.size - 1)).each.map do |j|
        a[i] > a[j] ? 1 : 0
     end.sum
   end.sum.even? ? 'YES' : 'NO'
end

t = gets.strip.to_i
for a0 in (0..t-1)
    n = gets.strip.to_i
    a = gets.strip
    a = a.split(' ').map(&:to_i)
    result = larrysArray(A)
    puts result
end
