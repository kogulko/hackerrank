#solution for https:#www.hackerrank.com/challenges/queens-attack-2/problem
#
#!/bin/ruby

def queensAttack(n, k, i_q, j_q, obstacles)
        rRObstacle = -1
        cRObstacle = -1
        rBRObstacle = -1
        cBRObstacle = -1
        rBObstacle = -1
        cBObstacle = -1
        rBLObstacle = -1
        cBLObstacle = -1
        rLObstacle = -1
        cLObstacle = -1
        rTLObstacle = -1
        cTLObstacle = -1
        rTObstacle = -1
        cTObstacle = -1
        rTRObstacle = -1
        cTRObstacle = -1

        #Total squares attacked by the queen
        reachableSquares = 0

        #Finds the closest object in each direction
        obstacles.each do |obstacle|
            rObstacle = obstacle.first
            cObstacle = obstacle.last

            #Right
            if((cObstacle < cRObstacle || rRObstacle == -1) && cObstacle > j_q && rObstacle == i_q)
                rRObstacle = rObstacle
                cRObstacle = cObstacle
                next
            end

            #Bottom Right
            if(i_q - rObstacle == cObstacle - j_q && cObstacle > j_q && rObstacle < i_q && ((rObstacle > rBRObstacle && cObstacle < cBRObstacle) || rBRObstacle == -1))
                rBRObstacle = rObstacle
                cBRObstacle = cObstacle
                next
            end

            #Bottom
            if((rObstacle > rBObstacle || rBObstacle == -1) && rObstacle < i_q && cObstacle == j_q)
                rBObstacle = rObstacle
                cBObstacle = cObstacle
                next
            end

            #Bottom Left
            if(i_q - rObstacle == j_q - cObstacle && cObstacle < j_q && rObstacle < i_q && ((rObstacle > rBLObstacle && cObstacle > cBLObstacle) || rBLObstacle == -1))
                rBLObstacle = rObstacle
                cBLObstacle = cObstacle
                next
            end

            #Left
            if((cObstacle > cLObstacle || rLObstacle == -1) && cObstacle < j_q && rObstacle == i_q)
                rLObstacle = rObstacle
                cLObstacle = cObstacle
                next
            end

            #Top Left
            if(j_q - cObstacle == rObstacle - i_q && cObstacle < j_q && rObstacle > i_q && ((rObstacle < rTLObstacle && cObstacle > cTLObstacle) || rTLObstacle == -1))
                rTLObstacle = rObstacle
                cTLObstacle = cObstacle
                next
            end

            #Top
            if((rObstacle < rTObstacle || rTObstacle == -1) && rObstacle > i_q && cObstacle == j_q)
                rTObstacle = rObstacle
                cTObstacle = cObstacle
                next
            end

            #Top Right
            if(rObstacle - i_q == cObstacle - j_q && cObstacle > j_q && rObstacle > i_q && ((rObstacle < rTRObstacle && cObstacle < cTRObstacle) || rTRObstacle == -1))
                rTRObstacle = rObstacle
                cTRObstacle = cObstacle
                next
            end

        end

        #Calculates the distance to the closest obstacle in each direction and adds it to reachableSquares
        #R B L T
        reachableSquares += (cRObstacle != -1) ? (cRObstacle - j_q -1) : n - j_q
        reachableSquares += (rBObstacle != -1) ? (i_q - rBObstacle - 1) : i_q - 1
        reachableSquares += (cLObstacle != -1) ? (j_q - cLObstacle -1) : j_q - 1
        reachableSquares += (rTObstacle != -1) ? (rTObstacle - i_q - 1) : n - i_q

        #BR BL TL TR
        reachableSquares += (cBRObstacle != -1) ? (cBRObstacle - j_q -1) : [n - j_q, i_q - 1].min
        reachableSquares += (rBLObstacle != -1) ? (j_q - cBLObstacle - 1) : [j_q - 1, i_q - 1].min
        reachableSquares += (cTLObstacle != -1) ? (j_q - cTLObstacle -1) : [j_q - 1, n - i_q].min
        reachableSquares += (rTRObstacle != -1) ? (cTRObstacle - j_q - 1) : [n - j_q, n - i_q].min
        reachableSquares
end

n, k = gets.strip.split(' ')
n = n.to_i
k = k.to_i
r_q, c_q = gets.strip.split(' ')
r_q = r_q.to_i
c_q = c_q.to_i
obstacles = Array.new(k)
for obstacles_i in (0..k-1)
  obstacles_t = gets.strip
  obstacles[obstacles_i] = obstacles_t.split(' ').map(&:to_i)
end
result = queensAttack(n, k, r_q, c_q, obstacles)
puts result
