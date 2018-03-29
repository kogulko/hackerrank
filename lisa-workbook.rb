# solution for https://www.hackerrank.com/challenges/lisa-workbook/problem
#
def workbook(n, k, arr)
  count = 0
  page = 0
  arr.each do |problems|
    1.upto(problems) do |i|
      if k == 1
        page += 1
        count +=1
      else
        page += 1 if i % k == 1
        count += 1 if page == i
      end
    end
  end
  count
    # Complete this function
end

n, k = gets.strip.split(' ')
n = n.to_i
k = k.to_i
arr = gets.strip
arr = arr.split(' ').map(&:to_i)
result = workbook(n, k, arr)
puts result
