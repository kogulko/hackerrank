# solution for https://www.hackerrank.com/challenges/almost-sorted/forum
#
#
# (1)input the array in vector

# (2)run through the vector from index 1 to len-2 ( leaving the first and last elements)

# (3)At each of these indices check whether it forms an inversion or a reverse inversion. Inversion is if curr > prev && curr > next. Similarly find out reverse inversions, curr < prev && curr < next. I call inversions as dips, and reverse inversions as ups.

# (4)for the first and last elements you can check only the next and prev respectively as they are at the boundary.

# (5)Once you have collected data of these inversions, if you analyze you will see that if reverse has to form a soln, you will have only one dip and one up.

# (6)And if swapping can be soln then there will be 2 dips and 2 ups.

# (7)If you get more than 2 dips and 2ups, it means it can't be solved.

# (8)There are some edge cases which you need to take care of though.
#
def almostSorted(a)
  ups = []
  dips = []
  a.each_index do |i|
    next if i == 0 || i == a.size - 1
    if a[i] > a[i - 1] && a[i] > a[i + 1]
      dips << i
    elsif a[i] < a[i - 1] && a[i] < a[i + 1]
      ups << i
    end
  end
  if a.last < a.first
    2.times do
      dips.unshift(0)
      ups.push(a.size - 1)
    end
  end
  puts "#{ups.inspect} #{dips.inspect}"
  if dips.empty? && ups.empty?
    puts "yes"
  elsif dips.size == 1 && ups.size == 1 && ups.first > a.first && dips.first < a.last
    puts "yes"
    operator = ((dips.first - ups.first).abs == 1 ? 'swap' : 'reverse')
    puts "#{operator} #{dips.first + 1} #{ups.first + 1}"
  elsif dips.size == 2 && ups.size == 2 && (ups.sum  - dips.sum).abs == 2
    puts "yes"
    puts "swap #{dips.first + 1} #{ups.last + 1}"
  else
    puts 'no'
  end
end

n = gets.strip.to_i
arr = gets.strip
arr = arr.split(' ').map(&:to_i)
almostSorted(arr)
