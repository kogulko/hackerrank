# solution for https://www.hackerrank.com/challenges/cavity-map/problem
#

def cavityMap(n, grid)
  visited = []
  1.upto(n-2) do |i|
    1.upto(n-2) do |j|
      next if visited.include?([i,j])
      if grid[i][j] > [grid[i+1][j], grid[i-1][j],grid[i][j+1],grid[i][j-1]].max
        visited += [[i+1, j], [i-1, j],[i, j+1], [i, j-1]]
        grid[i][j] = 'X'
      end
    end
  end
  grid.map(&:join)
    # Complete this function
end

n = gets.strip.to_i
grid = Array.new(n)
for grid_i in (0..n-1)
  grid[grid_i] = gets.strip.split(//).map(&:to_i)
end
result = cavityMap(n, grid)
print result.join("\n")
