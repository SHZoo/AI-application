path(Start, Goal):- path([Start], [], Goal).
path([], _, _ ):-
   write('Queue empty: no solution found').
path([Goal | RestofQueue], _ , Goal):- 
   nl, write('Solution found: '), write(Goal).
path([State | RestofQueue], AlreadySeen, Goal):- 
   write('Present state: '), 
   write(State), 
   nl,
   (bagof(Successor, moves(State, RestofQueue, AlreadySeen, Successor), SuccessorList); SuccessorList = []),
   append(RestofQueue, SuccessorList, NewQueue),
   !,
   path(NewQueue, [State | AlreadySeen], Goal).
moves(State, Queue, AlreadySeen, NewState):-
   move(State, NewState),
   NewState \== State,
   not(member(NewState, Queue)),
   not(member(NewState, AlreadySeen)).
member(X, [X | _ ]).
member(X, [ _ | T ]):- member(X, T).
append([], List, List).
append([Head | Tail], List, [Head | NewTail]):-append(Tail, List, NewTail).

move(1,2).
move(1,3).
move(2,4).
move(2,5).
move(3,6).
move(3,7).
move(4,8).
move(4,9).
move(5,10).
move(5,11).
move(6,12).
move(6,13).
move(7,14).
move(7,15).
