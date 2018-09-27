"
" This function takes any drivel and returns Bob's response.
"
function! Answer(drivel) abort
  if a:drivel =~# '\v[A-Z]' && a:drivel !~# '\v[a-z]'
    return 'Whoa, chill out!'
  elseif a:drivel =~# '\v.*\?\s*$'
    return 'Sure.'
  elseif a:drivel =~# '\v^\s*$'
    return 'Fine. Be that way!'
  else
    return 'Whatever.'
  endif
endfunction
