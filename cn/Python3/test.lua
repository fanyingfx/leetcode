function f(n,m)
    if n == 1 then
        return m
    end
    return f(n-1,n*m)
end
f(100000,1)