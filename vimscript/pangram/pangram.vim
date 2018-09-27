function! IsPangram(sentence) abort
  return len(uniq(sort(split(
        \ substitute(tolower(a:sentence), '\v[^a-z]', '', 'g'),
        \ '\zs')))) == 26
endfunction
