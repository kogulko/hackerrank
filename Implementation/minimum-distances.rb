#solution for https://www.hackerrank.com/challenges/minimum-distances/problem

def minimumDistances(a)
  # Create empty dictionary to keep track of element value and its last know position in the array
  d = []

  # Initialize minimum difference variable as one more than the maximum value(n-1) we can achieve
  min_diff = a.size

  # Going through each element in the array
  a.each_with_index do |num, i|
    # Try/Except statement to find record of the last known index for the element in the dictionary(for index difference calc), if unable to find the record then create the record
    if d[num]
      # min_diff equals minimum value between (the element index i and the last known location of the same element) and (min_diff)
      min_diff = [i-d[num],min_diff].min
      # Now if min_diff has value 1 then the code doesnt need to go further as its the minimum possible value for the answer
      break if min_diff == 1
    end
    # Change the last known position of the element
    d[num]=i
  end
  # If min_diff is the same as initialized value meaning no element in input array is repeating then print -1 else the minimum difference value
  min_diff == a.size ? -1 : min_diff
end

# n = gets.strip.to_i
a = gets.strip
a = a.split(' ').map(&:to_i)
result = minimumDistances(a)
puts result
