# solution for https://www.hackerrank.com/contests/w37/challenges/dynamic-line-intersection/problem

def dynamicLineIntersection(lines)
  equations = Hash.new(0)
  res = []
  lines.each do |operator, k ,b|
    if operator == '+'
      equations["#{k} #{b}"] += 1
    elsif operator == '-'
      equations["#{k} #{b}"] -= 1
    else
      res << equations.map do |key, value|
        l, c = key.split(' ').map(&:to_i)
        (k.to_i - c).fdiv(l) % 1 == 0 ? value : 0
      end.sum
    end
  end
  res
end

def dynamicLineIntersection(lines)
  # equations = Hash.new(0)
  # folds = {}
  # lines.each do |operator|


  # end
end

def add_folds(equations, lines_int, k, b)
  count = 0
  res = []
  (0..100000).each do |y|
    if (y - b) % k == 0
      equations[y.to_s] += 1
      
    end
  end
end

n = gets.to_i
lines = []
n.times do
  lines << gets.strip.split(' ')
end

puts dynamicLineIntersection(lines)

