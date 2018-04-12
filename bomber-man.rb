#solution for https://www.hackerrank.com/challenges/bomber-man/problem
#
##
#A few useful tricks for this problem:

#If N = 1, then we just print the initial board, as Bomberman hasn't put any new bombs on it;

#If we look at the board starting from second N = 2, we'll see a pattern. On every even time N, Bomberman will fill the empty spaces with bombs and, on every odd time N, he will observe some of them exploding. Then, without doing any unnecessary computation, we can say for sure that, if N is even, then the board will be full of bombs;

#If you look at the remaining possible values of N (N >= 3 and N is odd), you'll see that there's a very clear pattern. Thanks to it, you can assure that there are only two possibilities of board configurations for those values and deciding between them is as easy as applying a simple math operator to N;

#Using these previous 3 tips, you can simplify your problem. Instead of keeping track of the number of seconds remaining for a bomb to detonate, you can just keep an eye on those that will explode next.

def bomberMan(n, a, r, c)
  n.even? ? r.times.map {'O'* c }  : ( n == 1 ? a : (n % 4 == 1 ? detonate(detonate(a)) : detonate(a)) )
end


def detonate(a)
  bombs = []
  a.each_index do |i|
    a[i].chars.each_index do |j|
      bombs << [i, j] if a[i][j] == 'O'
      a[i][j] = 'O'
    end
  end
  bombs.each { |i,j| boom(a,i,j) }
  a
end

def boom(a,i,j)
  a[i][j] = '.'
  [-1, 1].each do |c|
    a[i + c][j] = '.' if (i+c) > -1 && a[i + c]
    a[i][j + c] = '.' if (j+c) > -1 && a[i][j + c]
  end
end


r, c, n = gets.strip.split(' ')
r = r.to_i
c = c.to_i
n = n.to_i
a = Array.new(r)
for a_i in (0..r-1)
  a[a_i] = gets.strip
end
result = bomberMan(n, a, r, c)
print result.join("\n")
