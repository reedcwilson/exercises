function! ToRna(strand) abort
  if a:strand =~# '[^GCTA]'
    return ''
  endif
  return tr(a:strand, 'GCTA', 'CGAU')
endfunction
