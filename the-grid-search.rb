#solution for https://www.hackerrank.com/challenges/the-grid-search/problem
#
def gridSearch(g, p)
  g.each_with_index do |row, index|
    if start = row.index(p.first)
      success = true
      g[(index + 1)..(index + p.size - 1)].each_with_index do |subr, subin|
        if subr[start..-1].start_with?(p[1+subin])
          next
        else
          success = false
          break
        end
      end
      return 'YES' if success
    else
      next
    end
  end
  return 'NO'

end

t = gets.strip.to_i
(t-1).times do
  r, c = gets.strip.split(' ')
  r = r.to_i
  c = c.to_i
  g = Array.new(r)
  for g_i in (0..r-1)
    g[g_i] = gets.strip
  end
  r, c = gets.strip.split(' ')
  r = r.to_i
  c = c.to_i
  p = Array.new(r)
  for p_i in (0..r-1)
    p[p_i] = gets.strip
  end
  result = gridSearch(g, p)
  puts result
end

