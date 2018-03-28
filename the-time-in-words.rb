#solution for https://www.hackerrank.com/challenges/the-time-in-words/problem
#
#

NUMBERS = [
  "o' clock",
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
  "ten",
  "eleven",
  "twelve",
  "thirteen",
  "fourteen",
  "quarter",
  "sixteen",
  "seventeen",
  "eighteen",
  "nineteen",
  "twenty",
  "twenty one",
  "twenty two",
  "twenty three",
  "twenty four",
  "twenty five",
  "twenty six",
  "twenty seven",
  "twenty eight",
  "twenty nine",
  "half"
]

def timeInWords(h, m)
  case m
  when 0
    [NUMBERS[h % 12], NUMBERS[m]]* " "
  when 1..14, 16..29
    "#{NUMBERS[m]} minute#{m == 1 ? '' : 's'} past #{NUMBERS[h % 12]}"
  when 15, 30
    "#{NUMBERS[m]} past #{NUMBERS[h % 12]}"
  when 45
    "#{NUMBERS[60 - m]} to #{NUMBERS[(h + 1) % 12]}"
  when 31..44, 46..59
    "#{NUMBERS[60 - m]} minute#{m == 59 ? '' : 's'} to #{NUMBERS[(h + 1) % 12]}"
  end
  # Complete this function
end

h = gets.strip.to_i
m = gets.strip.to_i
result = timeInWords(h, m)
puts result
