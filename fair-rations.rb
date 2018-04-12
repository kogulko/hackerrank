# solution for https://www.hackerrank.com/challenges/fair-rations/problem
# In this problem the thing is if sum of all number is even ,then array can be even. if sum of all number is odd , then the answer is NO.

def fairRations(b)
  return 'NO' if b.sum.odd?
  b.each_index.map do |i|
    if b[i].odd?
      b[i] += 1
      b[i+1] += 1
      2
    else
      0
    end
  end.sum
end

n = gets.strip.to_i
b = gets.strip
b = b.split(' ').map(&:to_i)
result = fairRations(B)
puts result
