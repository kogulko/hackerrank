#solution for https://www.hackerrank.com/contests/w37/challenges/the-average-rating-of-top-employees
#
#
def averageOfTopEmployees(rating)
  arr = rating.select { |a| a >= 90 }
  puts ("%.2f" % (((arr.sum / arr.size.to_f) * 100).round)/100.0)
end

n = gets.to_i

rating = Array.new(n)

n.times do |rating_itr|
    rating_item = gets.to_i
    rating[rating_itr] = rating_item
end

averageOfTopEmployees rating
