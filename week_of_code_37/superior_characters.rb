

# Complete the maximumSuperiorCharacters function below.
def maximumSuperiorCharacters(freq)
    sum = freq.sum
    return 0 if sum.zero?
    ceil_half = (sum / 2.0).ceil
    current_sum = 0
    freq.each_with_index do |f,i|
      current_sum += f
      if current_sum >= ceil_half
        result = freq[(i+1)..-1].sum
        tail = f - (current_sum - ceil_half)
        result += [f - tail, (sum - ceil_half) - tail].min
        result -= 1 if sum.even?
        return result
      end

    end
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

t = gets.to_i

t.times do |t_itr|
  freq = gets.rstrip.split(' ').select { |a| a != '0' }.map(&:to_i)

    result = maximumSuperiorCharacters freq

    fptr.write result
    fptr.write "\n"
end

fptr.close()

