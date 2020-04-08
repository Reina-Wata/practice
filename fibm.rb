def matmul(a,b)
  [[a[0][0]*b[0][0]+a[0][1]*b[1][0],
    a[0][0]*b[0][1]+a[0][1]*b[1][1]],
   [a[1][0]*b[0][0]+a[1][1]*b[1][0],
    a[1][0]*b[0][1]+a[1][1]*b[1][1]]]
end

def matsquare(a)
  matmul(a,a)
end

def matpower(a,n)
  if n==0
    [[1,0],[0,1]]
  else
    if n%2==1
      matmul(a,matpower(a,n-1))
    else
      matsquare(matpower(a,n/2))
    end
  end
end

def fibm(k)
  q=[[1,1],[1,0]]
  matpower(q,k)[1][0]+matpower(q,k)[1][1]
end

def fibm6(k)
  q=[[1,1],[1,0]]
  (matpower(q,k)[1][0]+matpower(q,k)[1][1])%1000000
end

