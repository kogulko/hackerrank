# solution for https://www.hackerrank.com/challenges/manasa-and-stones/problem
#
def stones(n, a, b)
    d = (a-b).abs
    return [(n-1) * a] if d.zero?
    current = [a,b].min
    0.upto(n-1).map { |i| (n-1) * current + i * d }
    # Complete this function
end

t = gets.strip.to_i
for a0 in (0..t-1)
    n = gets.strip.to_i
    a = gets.strip.to_i
    b = gets.strip.to_i
    result = stones(n, a, b)
    puts result.join(" ")
end

