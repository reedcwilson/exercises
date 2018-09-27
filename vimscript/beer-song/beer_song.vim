let s:strings = "
      \No more bottles of beer on the wall, no more bottles of beer.\n
      \Go to the store and buy some more, 99 bottles of beer on the wall.
      \#
      \1 bottle of beer on the wall, 1 bottle of beer.\n
      \Take it down and pass it around, no more bottles of beer on the wall.
      \#
      \2 bottles of beer on the wall, 2 bottles of beer.\n
      \Take one down and pass it around, 1 bottle of beer on the wall.
      \#
      \%s bottles of beer on the wall, %s bottles of beer.\n
      \Take one down and pass it around, %s bottles of beer on the wall."

let s:strings = split(s:strings, '#')

function! Verse(verse) abort
  let l:verse = s:strings[min([3, a:verse])]
  if l:verse =~# '%'
    return printf(l:verse . "\n", a:verse, a:verse, a:verse - 1)
  endif
  return printf(l:verse . "\n")
endfunction

function! Verses(start, end) abort
  let l:verses = map(reverse(range(a:end, a:start)), 'Verse(v:val)')
  return join(l:verses, "\n")
endfunction
