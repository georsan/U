function my_trapezoidal_function_Sandoval_Jorge(fun,a,b,M)
    h=(b-a)/M;
    sum=0;
    for i=1:M-1
        x=a+i*h;
        sum=sum+fun(x);
    end
    trap=h*(fun(a)+2*sum+fun(b))/2;
    disp(trap)

end