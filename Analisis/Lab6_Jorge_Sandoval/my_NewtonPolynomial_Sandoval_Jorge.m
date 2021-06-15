function [c]=my_NewtonPolynomial_Sandoval_Jorge(X,Y)
    n=length(X);
    h=X(2)-X(1);
    f=zeros(n,n);
    f(:,1)=Y;
    for j=2:n
        for i=j:n
            f(i,j)=f(i,j-1)-f(i-1,j-1);
        end
    end
    
    c=f(n,n);
    for k=n-1:-1:1
        p=poly(X(1))/h;
        p(2)=p(2)-(k-1);
        c=conv(c,p)/k;
        m=length(c);
        c(m)=c(m)+f(k,k);
    end
    
end