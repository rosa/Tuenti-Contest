% Simple prefix expresion calculator in prolog

expr(A, A) :-
	number(A).

expr((=, A, B), N) :-
	expr(A,A1),
	expr(B,B1),
	N is A1 + B1.

expr((@, A), -A1) :-
	expr(A,A1).

expr((@, A, B), N) :-
	expr(A,A1),
	expr(B,B1),
	N is A1 - B1.
		
expr((#, A, B), N) :-
	expr(A,A1),
	expr(B,B1),
	N is A1 * B1.
