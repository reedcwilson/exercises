function! NucleotideCount(strand) abort
  if a:strand =~# '\v[^ACGT]'
    throw 'invalid nucleotide in strand'
  endif
  let l:counts = {'A':0, 'C':0, 'G':0, 'T':0}
  for l:key in keys(l:counts)
    let l:counts[l:key] = count(a:strand, l:key)
  endfor
  return l:counts
endfunction
