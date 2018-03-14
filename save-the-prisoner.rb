# solution for https://www.hackerrank.com/challenges/save-the-prisoner/problem
#!/bin/ruby

def saveThePrisoner(n, m, s)
    ans = (m + s - 1) - ((m + s - 1) / n) * n
    ans.zero? ? n : ans
end

t = gets.strip.to_i
for a0 in (0..t-1)
    n, m, s = gets.strip.split(' ')
    n = n.to_i
    m = m.to_i
    s = s.to_i
    result = saveThePrisoner(n, m, s)
    puts result;
end
