function! Valid(triangle) abort
  let [a, b, c] = a:triangle
  return count(a:triangle, 0) == 0 && 
        \ a + b >= c &&
        \ b + c >= a &&
        \ c + a >= b
endfunction

function! Check(triangle, func) abort
  return a:func(len(uniq(sort(copy(a:triangle)))))
endfunction

function! Equilateral(triangle) abort
  return Valid(a:triangle) && Check(a:triangle, {l -> l == 1})
endfunction

function! Isosceles(triangle) abort
  return Valid(a:triangle) && Check(a:triangle, {l -> l < 3})
endfunction

function! Scalene(triangle) abort
  return Valid(a:triangle) && Check(a:triangle, {l -> l == 3})
endfunction
