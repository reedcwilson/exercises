function! s:Prepare(word) abort
  return sort(split(tolower(a:word), '\zs'))
endfunction

function! Anagram(word, candidates) abort
  let l:word = s:Prepare(a:word)
  let l:anagrams = []
  for c in a:candidates
    if s:Prepare(c) ==? l:word && c !=? a:word
      let l:anagrams = add(l:anagrams, c)
    endif
  endfor
  return sort(l:anagrams)
endfunction
