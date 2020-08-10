def minesweeper(matrix):
    """ Counts neighboring bools of each index in a matrix within
        one index - including diagonals - and updates a matrix of zeroes
        to reflect that count.

        Parameters:
            matrix (array): matrix of boolean values
        Returns:
            z_matrix (array): altered values of matrix to reflect boolean neighbors

    """

  def sum_of_matr(matrix):
    """ Sums the value of a matrix.

        Parameters:
            matrix (array): array of arrays
        
        Returns:
            total (int): sum of the matrix values

    """ 
    total = sum([sum(x) for x in matrix])
    return total
  
  matr_hor = len(matrix[0])
  matr_vert = len(matrix)
  
  z_matr = [[0 for _ in range(matr_hor)] for _ in range(matr_vert)]
  
  cur_coord = [0, 0]
  
  while matr_vert > 0:
    
    while matr_hor > 0:
      
      if cur_coord[1] > 0: 
        
        if cur_coord[0] > 0:
          
          if cur_coord[0] < len(matrix) - 1:
            
            if cur_coord[1] < len(matrix[0]) - 1:
              surround = [matrix[i][cur_coord[1] - 1:cur_coord[1] + 2] \
                          for i in range(cur_coord[0]-1, cur_coord[0] + 2)]
              
              if matrix[cur_coord[0]][cur_coord[1]]:
                z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(surround) - 1
              else:
                z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(surround)

            else: 
              ver_edge = [matrix[i][cur_coord[1]-1:cur_coord[1]+1] \
                          for i in range(cur_coord[0] - 1, cur_coord[0] + 2)]
              
              if matrix[cur_coord[0]][cur_coord[1]]:
                z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(ver_edge) - 1
              else:
                z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(ver_edge)
          
          else:
            hor_edge = [matrix[i][cur_coord[1] - 1:cur_coord[1] + 2] \
                        for i in range(cur_coord[0] - 1,cur_coord[0] + 1)]
            
            if matrix[cur_coord[0]][cur_coord[1]]:
                z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(hor_edge) - 1
            else:
                z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(hor_edge)
        
        elif cur_coord[1] == len(matrix[0]) - 1:
          corner = [matrix[i][cur_coord[1] - 1: cur_coord[1] + 1] \
                    for i in range(0,2)]
          
          if matrix[cur_coord[0]][cur_coord[1]]:
                z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(corner) - 1
          else:
                z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(corner)
        
        else:
          hor_edge = [matrix[i][cur_coord[1] - 1:cur_coord[1] + 2] \
                      for i in range(cur_coord[0], cur_coord[0] + 2)]
          
          if matrix[cur_coord[0]][cur_coord[1]]:
              z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(hor_edge) - 1
          else:
              z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(hor_edge)
      
      elif cur_coord[0] == 0:
        corner = [matrix[i][0: 2] for i in range(0,2)]
        
        if matrix[cur_coord[0]][cur_coord[1]]:
            z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(corner) - 1
        else:
            z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(corner)

      elif cur_coord[0] == len(matrix) - 1:
        corner = [matrix[i][0:2] for i in range(cur_coord[1] - 2, cur_coord[1])]
        
        if matrix[cur_coord[0]][cur_coord[1]]:
            z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(corner) - 1
        else:
            z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(corner)

      else:
        ver_edge = [matrix[i][cur_coord[1]: cur_coord[1] + 2] \
                    for i in range(cur_coord[0] - 1, cur_coord[0] + 2)]
        
        if matrix[cur_coord[0]][cur_coord[1]]:
            z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(ver_edge) - 1
        else:
            z_matr[cur_coord[0]][cur_coord[1]] = sum_of_matr(ver_edge)
      
      matr_hor -= 1
      cur_coord[1] += 1
    
    cur_coord[0] += 1
    cur_coord[1] = 0
    matr_hor = len(matrix[0])
    matr_vert -= 1
  
  return z_matr