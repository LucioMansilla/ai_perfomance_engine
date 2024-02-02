module nqueens
open util/integer

sig Queen {
  row : Int,
  col: Int
} 

fact {
  all q: Queen{
    q.row >= 0 && q.row < #Queen
	  q.col >= 0 && q.col < #Queen
  }
}

pred noOverlap(q1,q2 : Queen) {
  q1.row != q2.row
  q1.col != q2.col
}


pred noDiagonalAttacks(q1,q2 : Queen) {
  minus[q1.row, q2.row] != minus[q1.col,q2.col]
  minus[q1.row, q2.row] != minus[q2.col,q1.col]
}
/*
 or row1 - col1 == row2 - col2  # same row
            or row1 + col1 == row2 + col2
*/
pred noDiagonalAttacks2(q1,q2 : Queen){
    minus[q1.row,q1.col] != minus[q2.row,q2.col]
    plus[q1.row,q1.col] != plus[q2.row,q2.col]
}
pred valid {
  all q1,q2 : Queen | q1 != q2 => noDiagonalAttacks2[q1, q2] and noOverlap[q1,q2]
}


//change bitwidth to 10

run valid for exactly 16 Queen, 6 Int, 10 seq
 

//[5,9,2,0,7,4,1,8,6,3]