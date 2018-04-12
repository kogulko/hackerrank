# solution for https://www.hackerrank.com/challenges/strange-code/problem
#
def strangeCode(t)
    # Complete this function
  rem = 3
  while t > rem do
    t -= rem
    rem *= 2
  end

  rem-t+1
end

t = gets.strip.to_i
result = strangeCode(t)
puts result
