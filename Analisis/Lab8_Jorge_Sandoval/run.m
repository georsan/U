% a)
Y=@(x) 60*x.^45-32*x.^33+233*x^5-47*x^2-77;
X=1/sqrt(3);
tol=0.0001;
[L,n]=program1(Y,X,tol);
%%
% b)
Y2=@(x) tan(cos((sqrt(5)+sin(x))/1+x.^2));
X2=(1+sqrt(5))/3;
[L,n]=program1(Y2,X2,tol);

%%
% c)
Y3=@(x) sin(x.^3-7*x.^2+6*x+8);
X3=(1-sqrt(5))/2;
[L,n]=program1(Y3,X3,tol);
%%
