function [C]=my_LagrangePolynomial_Sandoval_Jorge(X,Y)
n=length(X);
N=n-1;
L=zeros(n,n);
for i=1:N+1
    V=1;
    for j=1:N+1
        if i~=j
            V=conv(V,poly(X(j)))/(X(i)-X(j));
        end
    end
    L(i,:)=V;
end
C=Y*L;
end