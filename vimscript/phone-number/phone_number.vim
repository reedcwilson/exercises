function! ToNANP(number) abort
  let l:number = substitute(a:number, '\v[^0-9]', '', 'g')
  if match(l:number, '\v^1?[2-9][0-9]{2}[2-9][0-9]{6}$')
    let l:number = ''
  endif
  return strlen(l:number) ==# 11 ? l:number[1:] : l:number
endfunction
