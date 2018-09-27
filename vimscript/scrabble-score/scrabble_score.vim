let s:scores = {
      \ 1: ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'],
      \ 2: ['d', 'g'],
      \ 3: ['b', 'c', 'm', 'p'],
      \ 4: ['f', 'h', 'v', 'w', 'y'],
      \ 5: ['k'],
      \ 8: ['j', 'x'],
      \ 10: ['q', 'z']
      \}

let s:letters = {}
for [k, v] in items(s:scores)
  for l in v
    let s:letters[l] = str2nr(k)
  endfor
endfor

function! Score(word) abort
  let l:score = 0
  for l:c in split(tolower(a:word), '\zs')
    let l:score += s:letters[l:c]
  endfor
  return l:score
endfunction
