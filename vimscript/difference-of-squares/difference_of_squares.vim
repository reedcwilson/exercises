function! Difference(number) abort
  return SquareOfSum(a:number) - SumOfSquares(a:number)
endfunction

function! SquareOfSum(number) abort
  let l:sum = 0
  for l:n in range(1, a:number)
    let l:sum += l:n
  endfor
  return float2nr(pow(l:sum, 2))
endfunction

function! SumOfSquares(number) abort
  let l:sum = 0
  for l:n in range(1, a:number)
    let l:sum += pow(l:n, 2)
  endfor
  return float2nr(l:sum)
endfunction
