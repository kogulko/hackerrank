# solutin for https://www.hackerrank.com/challenges/3d-surface-area/problem



def surfaceArea(h, w, a)
  # Bottom and top area
  area = 2* h * w

  # Side area is just the sum of differences
  # between adjacent cells. Be careful not to
  # count a side twice.
  1.upto(h + 1) do |i|
    1.upto(w + 1) do |j|
      area += (a[i][j] - a[i-1][j]).abs
      area += (a[i][j] - a[i][j-1]).abs
    end
  end

  area
end

h, w = gets.strip.split(' ')
h = h.to_i
w = w.to_i
a = Array.new(h)
for a_i in (0..h-1)
  a_t = gets.strip
  a[a_i] = a_t.split(' ').map(&:to_i)
end
# Pad the grid width a layer of 0
# for easier calculation
a.unshift(Array.new(w) { 0 })
a.push(Array.new(w) { 0 })
a.each { |arr| arr.push(0); arr.unshift(0) }

result = surfaceArea(h, w, a)
puts result
