#solution for https://www.hackerrank.com/challenges/two-pluses/problem
#
#maximum product of 3 https://tproger.ru/problems/max-multiplication-of-three-numbers/

def twoPluses(grid)
  areas = []
  grid.each_index do |i|
    grid[i].chars.each_index do |j|
      explore(grid, i, j, areas) if grid[i][j] == 'G'
    end
  end
  areas.combination(2).map { |i,j| (i[:indexes] & j[:indexes]).empty? ? i[:area] * j[:area] : 0 }.max
end

def explore(grid, i, j, areas)
  area = { area: 1, indexes: [[i,j]] }
  size = 1
  loop do
    if exist?(i, j, size, grid) && [grid[i + size][j], grid[i - size][j], grid[i][j + size], grid[i][j - size]].all? { |cell| cell == 'G' }
      area[:area] += 4
      area[:indexes] << [i+size,j] << [i-size, j] << [i, j+size] << [i,j-size]
      size += 1
    else
      break
    end
  end
  areas << area
end

def exist?(i, j, size, grid)
  grid[i+size] && i - size > -1 && j - size > -1
end

n, m = gets.strip.split(' ')
n = n.to_i
m = m.to_i
grid = Array.new(n)
for grid_i in (0..n-1)
    grid[grid_i] = gets.strip
end
result = twoPluses(grid)
puts result
