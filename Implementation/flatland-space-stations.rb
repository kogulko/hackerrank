#solution for https://www.hackerrank.com/challenges/flatland-space-stations/problem
#
def flatlandSpaceStations(n, c)
  res = 1.upto(c.size - 1).map { |i| (c[i] - c[i-1]) / 2 }
  res << c.first unless c.first == 0
  res << n - 1 - c.last unless c.last == n - 1
  res.max.to_i
end

n, m = gets.strip.split(' ')
n = n.to_i
m = m.to_i
c = gets.strip
c = c.split(' ').map(&:to_i)
result = flatlandSpaceStations(n, c)
puts result

