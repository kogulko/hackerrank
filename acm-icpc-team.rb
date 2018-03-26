#solution for https://www.hackerrank.com/challenges/acm-icpc-team/problem problem
#

#!/bin/ruby

def acmTeam(topic)
    res = (0..(topic.size - 1)).to_a.combination(2).to_a.map do |a,b|
        (topic[a] | topic[b]).to_s(2).count('1')
    end
    [res.max, res.count(res.max)]
end

n, m = gets.strip.split(' ')
n = n.to_i
m = m.to_i
topic = Array.new(n)
for topic_i in (0..n-1)
    topic[topic_i] = gets.strip.to_i(2)
end
result = acmTeam(topic)
print result.join("\n")
