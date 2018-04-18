# solution for https://www.hackerrank.com/contests/w37/challenges/simple-language
#
#
def maximumProgramValue(commands)
  x = 0
  commands.each do |command|
    command, value = command.split(' ')
    new_value = (command == 'add' ? x + value.to_i : value.to_i)
    x = [new_value, x].max
  end
  x
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

commands = []
n = gets.to_i
n.times do
  commands << gets.strip
end


result = maximumProgramValue commands

fptr.write result
fptr.write "\n"

fptr.close()
