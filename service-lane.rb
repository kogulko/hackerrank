#solution for https://www.hackerrank.com/challenges/service-lane/problem


def serviceLane(width, cases)
  cases.map { |c| width[c.first..c.last].min }
    # Complete this function
end

n, t = gets.strip.split(' ')
n = n.to_i
t = t.to_i
width = gets.strip
width = width.split(' ').map(&:to_i)
cases = Array.new(t)
for cases_i in (0..t-1)
    cases_t = gets.strip
    cases[cases_i] = cases_t.split(' ').map(&:to_i)
end
result = serviceLane(width, cases)
print result.join("\n")

