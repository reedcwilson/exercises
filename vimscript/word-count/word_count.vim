function! WordCount(phrase) abort
  let l:words = {}
  for l:word in split(tolower(a:phrase), '\v[^A-Za-z0-9'']+')
    let l:w = substitute(l:word, '\v^''*|''*$', '', 'g')
    let l:words[l:w] += has_key(l:words, l:w)
  endfor
  return l:words
endfunction
