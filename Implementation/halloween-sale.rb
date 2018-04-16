#solution for https://www.hackerrank.com/challenges/halloween-sale/problem
#
def howManyGames(p, d, m, s)
  count = 0
  loop do
    price = p - d * count
    s -= (price < m ? m : price)
    break if s < 0
    count+=1
  end
  count
    # Return the number of games you can buy
end

p, d, m, s = gets.strip.split(' ')
p = p.to_i
d = d.to_i
m = m.to_i
s = s.to_i
answer = howManyGames(p, d, m, s)
puts answer
