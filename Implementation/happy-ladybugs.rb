# solution for https://www.hackerrank.com/challenges/happy-ladybugs/problem
#
#
# Complete the happyLadybugs function below.
#
#Happy Conditions:

# = There are at least one empty cell and there is no Letter with count 1

# OR

# = There is no empty cell but the given string is happy

def happyLadybugs(b)
  b.include?('_') && !("A".."Z").to_a.map { |letter| b.count(letter) }.include?(1) || happy?(b) ? 'YES' : 'NO'
    #
    # Write your code here.
    #

end

def happy?(b)
  b.each_index.count { |i| b[i] == b[(i-1).abs].to_s || b[i] == b[i+1].to_s } == b.size
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

g = gets.to_i

g.times do |g_itr|
    # n = gets.to_i

  b = gets.to_s.rstrip.split(//)

    result = happyLadybugs b

    fptr.write result
    fptr.write "\n"
end

fptr.close()
