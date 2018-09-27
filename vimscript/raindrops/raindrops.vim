function! Raindrops(number) abort
  let l:result = ''
  if fmod(a:number, 3) == 0
    let l:result = l:result . 'Pling'
  endif
  if fmod(a:number, 5) == 0
    let l:result = l:result . 'Plang'
  endif
  if fmod(a:number, 7) == 0
    let l:result = l:result . 'Plong'
  endif
  if l:result ==# ''
    return string(a:number)
  endif
  return l:result
endfunction
