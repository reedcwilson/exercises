function! Transform(scores) abort
  let l:new_letters = {}
  for [l:points, l:letters] in items(a:scores)
    for l:letter in l:letters
      let l:new_letters[tolower(l:letter)] = str2nr(l:points)
    endfor
  endfor
  return l:new_letters
endfunction
