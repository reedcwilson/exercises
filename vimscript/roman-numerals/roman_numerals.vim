let s:numerals = [ [1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
      \ [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'],
      \ [5, 'V'], [4, 'IV'], [1, 'I']]

function! ToRoman(number) abort
  let l:result = ''
  let l:number = a:number
  for [l:arab, l:num] in s:numerals
    let l:quot = float2nr(l:number / l:arab)
    let l:number = fmod(l:number, l:arab)
    let result .= repeat(l:num, l:quot)
  endfor
  return l:result
endfunction
