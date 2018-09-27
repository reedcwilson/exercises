function! LargestProduct(digits, span) abort
  if a:digits =~# '[^0-9]'
    throw 'invalid input'
  endif

  if a:span == 0
    return 1
  endif

  if a:span > strlen(a:digits) || a:span < 0
    return -1
  endif

  let l:products = []
  for l:i in range(0, strlen(a:digits) - a:span)
    let l:sublist = a:digits[l:i : (l:i + a:span) - 1]
    let l:product = 0
    execute('let l:product = ' . join(split(l:sublist, '\zs'), '*'))
    let l:products = add(l:products, l:product)
  endfor
  return max(l:products)
endfunction
