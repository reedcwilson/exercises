let s:alpha = 'abcdefghijklmnopqrstuvwxyz'
let s:key = 'zyxwvutsrqponmlkjihgfedcba'

function! AtbashDecode(cipher) abort
  let l:sentence = substitute(a:cipher, ' ', '', 'g')
  return tr(l:sentence, s:key, s:alpha)
endfunction

function! AtbashEncode(plaintext) abort
  let l:sentence = substitute(tolower(a:plaintext), '\v[^A-Za-z0-9]', '', 'g')
  let l:sentence = tr(l:sentence, s:alpha, s:key)
  let l:sentence = substitute(l:sentence, '\v(.....)', {m -> m[1] . ' '}, 'g')
  return substitute(l:sentence, '\v\s+$', '', 'g')
endfunction
