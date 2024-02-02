open util/ordering[State] as ord

/**
 * The missionaries and cannibals will be represented as Objects.
 */
abstract sig Object {}
sig Missionary, Cannibal extends Object {}

/**
 * The left and right relations contain the objects held on each
 * side of the river in a given state, respectively.
 */
sig State {
   left: set Object,
   right: set Object,
   boatOnLeft: one Bool
}

/**
 * In the initial state, all objects are on the left side and the boat is on the left side.
 */
fact initialState {
   let s0 = ord/first |
     s0.left = Object && no s0.right && s0.boatOnLeft = True
}

/**
 * Constrains at most two items to move from 'from' to 'to'.
 */
pred crossRiver [from, from", to, to": set Object] {
   
    (one x : from | {
       from" = from - x
       to" = to + x }) or
    // or the boat takes two items
    (some disj x,y : from | {
       from" = from - x - y
       to" = to + x + y })
}

/**
 * crossRiver transitions between states
 */
fact stateTransition {
  all s: State , s": ord/next[s] |
   (  not finalState[s]=> (
         True in s.boatOnLeft => (crossRiver[s.left, s".left, s.right, s".right] && s".boatOnLeft = False)
         else (crossRiver[s.right, s".right, s.left, s".left] && s".boatOnLeft = True))) and 
   (finalState[s] => s.left = s".left and s.right = s".right and s.boatOnLeft = s".boatOnLeft)
}

/**
 * all objects are moved to the right side of the river.
 */
pred solvePuzzle {
     some s : State | finalState[s]
} 

pred finalState[ s: State]{
	#s.right = 4

}
run solvePuzzle for 50 State, exactly 4 Missionary, exactly 4 Cannibal , 0 int ,exactly 2 Bool expect 1

/**
 * no Object can be in two places at once
 * this is implied by both definitions of crossRiver
 */
assert NoQuantumObjects {
   no s : State | some x : Object | x in s.left and x in s.right
}

check NoQuantumObjects for 8 State expect 0

/**
 * Define what happens when there are more cannibals than missionaries on either side of the river.
 */
fact eating { 
  all s: State | 
    (some Missionary & s.left => #(Missionary & s.left) >= #(Cannibal & s.left)) and 
    (some Missionary & s.right => #(Missionary & s.right) >= #(Cannibal & s.right))
}

sig Bool {}
one sig True, False extends Bool {}
