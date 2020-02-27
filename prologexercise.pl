%Author: Simon Parris%

parent(fred, sophusw). parent(fred, lawrence).
parent(fred, kenny). parent(fred, esther).
parent(inger,sophusw). parent(johnhs, fred).
parent(mads,johnhs). parent(lars, johan).
parent(johan,sophus). parent(lars,mads).
parent(sophusw,gary). parent(sophusw,john).
parent(sophusw,bruce). parent(gary, kent).
parent(gary, stephen). parent(gary,anne).
parent(john,michael). parent(john,michelle).
parent(addie,gary). parent(gerry, kent).
male(gary). male(fred).
male(sophus). male(lawrence).
male(kenny). male(esther).
male(johnhs). male(mads).
male(lars). male(john).
male(bruce). male(johan).
male(sophusw). male(kent).
male(stephen). female(inger).
female(anne). female(michelle).
female(gerry). female(addie).
father(X,Y):-parent(X,Y),male(X).
mother(X,Y):-parent(X,Y), female(X).

%Number 1
%siblings cant be parent to another sibling.%
sibling(X,Y) :- parent(Z,X),parent(Z,Y),not(X=Y).

%Number 2
%Displaying brothers of sophusw by entering brother(sophus,X).
brother(X,Y) :- male(X),sibling(X,Y).

%Number 3
%A niece is the daughter of a brother/sister or Brother in law/Sister in law.
niece(X,Y) :- female(X),parent(Z,X),sibling(Z,Y).

%Number 4
% Cousin a child of an uncle or aunt.
cousin(X,Y) :- sibling(A,B),parent(A,X),parent(B,Y).

%Number 5
% Describing an ancestor relationship
ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(X,Z),ancestor(Z,Y).

%Number 6
%Write a predicate called odd that returns true 
%if a list has an odd number of elements.

oddlist([_|X]) :- even([X]).
even([]).
evenlist([_|X]) :- odd([X]).

%Number 7
%Write a predicate that checks.
%for a palindrome.
palindrome([]).
palindrome([_]).
palindrome(LIST):-append([H|T],[H],LIST), palindrome(T).


%Number 8
%Show the substitution required to prove that sublist([a,b],[c,a,b]) is true.
sublist(X,Y) :- append(_,X,L), append(L,_Y).
append([],Y,Y).
append([H|T], Y,[H|L]) :- append(T,Y,L).
%Number 9 
%Write a predicate that computes the factorial of a number.
factorial(0,1).
factorial(N,F) :- N>0, N1 is N-1,factorial(N1,F1),F is N * F1.

%Number 10
%Compute the nth fibonacci number in exponential %time complexity.
fibexp(0, 1) :- !.
fibexp(1, 1) :- !.
fibexp(N, R) :- N1 is N - 1,N2 is N - 2,fibexp(N1, R1),fibexp(N2, R2),R is R1 + R2.

%Number 11
%%Compute the nth fibonacci number in linear %time complexity.
fib(1,1,0).
fib(2,1,1).
fib(N,V,PrevF) :- N>2,N1 is N-1,fib(N1,PrevF,LastPrevF),V is PrevF + LastPrevF.

%Number 12 
%Write a predicate the returns true %if a third list is the result of zipping two others together.
zip([],[],[]).
zip([A|TA],[B|TB],[Zip|TZip]) :- zip(TA,TB,TZip),Zip = pair(A,B).

%Number 13
%Write a predicate that counts the number of %times a specific atom appears in a list.
count(_,[],0).
count(X,[X|T],N) :- count(X,T,N1), N is N1+1.
count(X,[Y|T],N) :- not(X=Y), count(X,T,N).

%Number 14 
%Write a predicate that returns true %if a list is three copies of the same subset.
len(0,[]).
len(L+1, [_|T]) :- len(L,T).
div(L,X) :- append(X,X,K),append(K,X,L).
threecopies([]).
threecopies(LST) :- div(LST,_).