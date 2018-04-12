# solution for https://www.hackerrank.com/challenges/absolute-permutation/problem
#
#hint n = 100, k = 2
#Answer: 3 4 1 2 7 8 5 6 11 12 9 10 15 16 13 14 19 20 17 18 23 24 21 22 27 28 25 26 31 32 29 30 35 36 33 34 39 40 37 38 43 44 41 42 47 48 45 46 51 52 49 50 55 56 53 54 59 60 57 58 63 64 61 62 67 68 65 66 71 72 69 70 75 76 73 74 79 80 77 78 83 84 81 82 87 88 85 86 91 92 89 90 95 96 93 94 99 100 97 98

def absolutePermutation(n, k)
  if k == 0
    (1..n).to_a
  elsif n % (2*k) != 0
    [-1]
  else
    (1..n).step(2 * k).flat_map do |i|
      (k..(2*k - 1)).map { |j| i + j } + (0..(k - 1)).map { |j| i + j }
    end
  end
end


fptr = File.open(ENV['OUTPUT_PATH'], 'w')

t = gets.to_i

t.times do |t_itr|
    nk = gets.rstrip.split

    n = nk[0].to_i

    k = nk[1].to_i

    result = absolutePermutation n, k

    fptr.write result.join " "
    fptr.write "\n"
end

fptr.close()
