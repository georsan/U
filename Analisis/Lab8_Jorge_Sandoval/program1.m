function [L,n]=program1(f,x,toler)
 format long
 %Input ? f is the function input as a string ' f '
 % ? x is the dierentiation point
 % ? toler is the desired tolerance
 %Output ? L=[H' D' E']: H is the vector of step sizes
 % D is the vector of approximate derivatives
 % E is the vector of error bounds
 % ? n is the coordinate of the "best approimation"

 % NUMERICAL METHODS: MATLAB Programs
 %(c) 1999 by John H. Mathews and Kurtis D. Fink
 %To accompany the textbook:
 %NUMERICAL METHODS Using MATLAB,
 %by John H. Mathews and Kurtis D. Fink
 %ISBN 0?13?270042?5, (c) 1999
 %PRENTICE HALL, INC.
 %Upper Saddle River, NJ 07458

 max1=13;
 h=1/10;
 H(1)=h;
 D(1)=(feval(f,x+h)-feval(f,x-h))/(2*h);
 E(1)=0;
 R(1)=0;
 for n=1:2
 h=h/10;
 H(n+1)=h;
 D(n+1)=(feval(f,x+h)-feval(f,x-h))/(2*h);
 E(n+1)=abs(D(n+1)-D(n));
 R(n+1)=2*E(n+1)*(abs(D(n+1))+abs(D(n))+eps);
 end

 n=2;

 while((E(n)>E(n+1))&&(R(n)>toler))&&n<max1
 h=h/10;
 H(n+2)=h;
 D(n+2)=(feval(f,x+h)-feval(f,x-h))/(2*h);
 E(n+2)=abs(D(n+2)-D(n+1));
 R(n+2)=2*E(n+2)*(abs(D(n+2))+abs(D(n+1))+eps);
 n=n+1;
 end

 n=length(D)-1;
 L=[H' D' E'];
end