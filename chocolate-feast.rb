# solution for https://www.hackerrank.com/challenges/chocolate-feast/problem
#
def chocolateFeast(n, c, m)
  number = n/c
  wrapers = number
  loop do
    if wrapers < m
      return number
    else
      number += wrapers / m
      wrapers -= ((wrapers / m) * (m - 1))
    end
  end
    # Complete this function
end

t = gets.strip.to_i
t.times do
    n, c, m = gets.strip.split(' ')
    n = n.to_i
    c = c.to_i
    m = m.to_i
    result = chocolateFeast(n, c, m)
    puts result
end
